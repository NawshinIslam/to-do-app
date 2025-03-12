# app/routes.py
from flask import jsonify, request, render_template
from .models import add_task, get_tasks, delete_task, mark_task_done
from . import app  # Import the app instance

# Route to serve the frontend
@app.route('/')
def home():
    return render_template('index.html')

# API to add a new task
@app.route('/add_task', methods=['POST'])
def add_new_task():
    data = request.get_json()
    task_desc = data.get('task_desc')
    if task_desc:
        task_id = add_task(task_desc)
        return jsonify({"status": "success", "task_id": task_id})
    return jsonify({"status": "error", "message": "Task description is required"}), 400

# API to fetch all tasks
@app.route('/tasks', methods=['GET'])
def fetch_tasks():
    tasks = get_tasks()
    return jsonify({"status": "success", "tasks": tasks})

# API to delete a task
@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    delete_task(task_id)
    return jsonify({"status": "success"})

@app.route('/mark_task_done/<int:task_id>', methods=['PUT'])
def mark_task_done_by_id(task_id):
    mark_task_done(task_id)
    return jsonify({"status": "success"})