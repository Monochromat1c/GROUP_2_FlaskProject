# Priority To-Do List System

## Description
A web-based To-Do List application that helps users manage and prioritize tasks efficiently, ensuring productivity and organization.

## Features
- Add, edit, and delete tasks
- Set and update task priority (Low, Medium, High)
- Mark tasks as completed or pending
- Filter tasks by status and priority
- Persistent storage using a database

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Monochromat1c/GROUP_2_FlaskProject.git
    cd GROUP_2_FlaskProject
    ```

2. Navigate to the project directory.

3. Set up virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For iOS/Linux
    venv\Scripts\activate     # For Windows
    ```

4. Install dependencies:
    ```bash
    pip install flask
    ```

5. Run the application:
    ```bash
    python app.py
    ```

6. Open your web browser and visit:
    ```
    http://127.0.0.1:5000/
    ```

---

## User Guide

### Adding a New Task
- Enter the task description in the input field.
- Select the priority level: Low, Medium, or High.
- Click the **Add Task** button.

### Viewing Tasks
- Tasks appear below with their priority and completion status.

### Editing a Task
- Click the **Edit** button beside a task.
- Change the description or priority.
- Save to update the task.

### Marking Tasks Completed or Pending
- Use the checkbox next to a task to toggle its status.
- Completed tasks are visually distinct.

### Deleting a Task
- Click the **Delete** button to remove a task.

### Filtering Tasks
- Filter by status (Completed, Pending) or by priority level.

---

**Note:** All tasks are saved in the database, so they remain available across sessions.

## Technologies Used
- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, Tailwind CSS

## Roles & Contributors
| **Role**        | **Name**              | **Responsibilities**                                     |
|-----------------|-----------------------|----------------------------------------------------------|
| Project Leader  | Angela Arguelles      | Overall progress and presentation, documentation review  |
| Programmer      | Charles Manuel Diestro| Backend and frontend logic, database handling            |
| System Analyst  | Ian Gabriel Dichosa   | Feature planning, workflow design (flowchart)            |
| Tester          | Eliza Jane Hingco     | Bug testing                                              |
| Documenter      | Charles Cayetano      | README writing, submission folder management             |

## Future Improvements
- Add task reminders or notifications
- Allow task sharing and collaboration
- Improve filtering and sorting (e.g., by due date)
- Enhance the user interface with more customization
- Add user accounts for personalized task lists

## License
This project is open-source under the MIT License.