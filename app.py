"""
Task Manager API
A simple Flask REST API for managing tasks, built as a QA testing practice target.
Storage is in-memory (a Python list) - data resets every time the server restarts.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
tasks = []
next_id = 1


def find_task(task_id):
    """Helper: find a task by id, or return None if it doesn't exist."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def validate_task_data(data, partial=False):
    """
    Validate incoming task data.
    Returns an error message string if invalid, or None if valid.
    If partial=True, fields are optional (used for PUT updates).
    """
    if not isinstance(data, dict):
        return "Request body must be a JSON object"

    if "title" in data or not partial:
        title = data.get("title")
        if title is None or (isinstance(title, str) and title.strip() == ""):
            return "Title is required and cannot be empty"
        if not isinstance(title, str):
            return "Title must be a string"
        if len(title) > 100:
            return "Title cannot exceed 100 characters"

    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return "Completed must be a boolean (true or false)"

    if "description" in data and data["description"] is not None:
        if not isinstance(data["description"], str):
            return "Description must be a string"

    return None


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    error = validate_task_data(data, partial=False)
    if error:
        return jsonify({"error": error}), 400

    task = {
        "id": next_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "completed": data.get("completed", False),
    }
    tasks.append(task)
    next_id += 1

    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = find_task(task_id)
    if task is None:
        return jsonify({"error": f"Task with id {task_id} not found"}), 404
    return jsonify(task), 200


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = find_task(task_id)
    if task is None:
        return jsonify({"error": f"Task with id {task_id} not found"}), 404

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    error = validate_task_data(data, partial=True)
    if error:
        return jsonify({"error": error}), 400

    if "title" in data:
        task["title"] = data["title"]
    if "description" in data:
        task["description"] = data["description"]
    if "completed" in data:
        task["completed"] = data["completed"]

    return jsonify(task), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = find_task(task_id)
    if task is None:
        return jsonify({"error": f"Task with id {task_id} not found"}), 404

    tasks.remove(task)
    return "", 204


@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(405)
def handle_405(e):
    return jsonify({"error": "Method not allowed on this endpoint"}), 405


if __name__ == "__main__":
    app.run(debug=True, port=5000)