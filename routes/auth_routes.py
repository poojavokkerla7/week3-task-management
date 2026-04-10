from flask import Blueprint, request, jsonify
from models.user import users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    for user in users:
        if user["username"] == data["username"]:
            return jsonify({"error": "User already exists"}), 400

    users.append(data)
    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    for user in users:
        if user["username"] == data["username"] and user["password"] == data["password"]:
            return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": "Invalid username or password"}), 401
