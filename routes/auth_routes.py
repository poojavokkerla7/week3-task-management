from flask import Blueprint, request, jsonify
from models.user import users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "username" not in data or "password" not in data:
        return jsonify({"error": "Missing fields"}), 400

    for user in users:
        if user["username"] == data["username"]:
            return jsonify({"error": "User already exists"}), 400

    users.append({
        "username": data["username"],
        "password": data["password"]
    })

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for user in users:
        if user["username"] == data.get("username") and user["password"] == data.get("password"):
            return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": "Invalid credentials"}), 401
