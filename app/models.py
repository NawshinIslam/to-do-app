# app/models.py
from .database import get_db_connection

def add_task(task_desc):
    """Insert a new task and return its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_desc) VALUES (%s)", (task_desc,))
    task_id = cursor.lastrowid  # Get the last inserted task ID
    conn.commit()
    cursor.close()
    conn.close()
    return task_id

def get_tasks():
    """Fetch all tasks."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Return results as dictionaries
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

def delete_task(task_id):
    """Delete a task by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()

def mark_task_done(task_id):
    """Mark a task as done."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'Done' WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()