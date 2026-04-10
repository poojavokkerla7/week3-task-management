from flask import Blueprint, request, jsonify
from models.task import tasks

task_bp = Blueprint("task", __name__)

@task_bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks.append(data)
    return jsonify({"message": "Task added"}), 201


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@task_bp.route("/tasks/<int:index>", methods=["PUT"])
def update_task(index):
    if index < len(tasks):
        tasks[index] = request.json
        return jsonify({"message": "Task updated"})
    return jsonify({"error": "Task not found"}), 404


@task_bp.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"}), 404
