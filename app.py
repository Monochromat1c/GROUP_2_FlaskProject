from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                priority TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()
        conn.close()

# Initialize the database when the app starts
with app.app_context():
    init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    priority_filter = request.args.get('priority')
    
    if priority_filter and priority_filter != 'all':
        if priority_filter == 'Completed':
            todos = conn.execute('SELECT * FROM todos WHERE completed = 1 ORDER BY id DESC').fetchall()
        else:
            todos = conn.execute('SELECT * FROM todos WHERE priority = ? ORDER BY id DESC', (priority_filter,)).fetchall()
    else:
        todos = conn.execute('SELECT * FROM todos ORDER BY id DESC').fetchall()
    
    completed_weekly = conn.execute('SELECT COUNT(*) FROM todos WHERE completed = 1 AND created_at >= date(CURRENT_DATE, "-7 days")').fetchone()[0]
    completed_monthly = conn.execute('SELECT COUNT(*) FROM todos WHERE completed = 1 AND strftime("%Y-%m", created_at) = strftime("%Y-%m", CURRENT_DATE)').fetchone()[0]
    completed_yearly = conn.execute('SELECT COUNT(*) FROM todos WHERE completed = 1 AND strftime("%Y", created_at) = strftime("%Y", CURRENT_DATE)').fetchone()[0]
    
    conn.close()
    return render_template('index.html', todos=todos, current_filter=priority_filter,
                           completed_weekly=completed_weekly,
                           completed_monthly=completed_monthly,
                           completed_yearly=completed_yearly)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form['task']
    priority = request.form['priority']
    conn = get_db_connection()
    conn.execute('INSERT INTO todos (task, priority) VALUES (?, ?)', (task, priority))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    conn = get_db_connection()
    if request.method == 'POST':
        task = request.form['task']
        priority = request.form['priority']
        completed = 'completed' in request.form 
        conn.execute('UPDATE todos SET task = ?, priority = ?, completed = ? WHERE id = ?', (task, priority, completed, todo_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    todo = conn.execute('SELECT * FROM todos WHERE id = ?', (todo_id,)).fetchone()
    conn.close()
    return render_template('edit.html', todo=todo)

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
