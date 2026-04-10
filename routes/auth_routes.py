from flask import Blueprint, request, jsonify
from models.user import add_user, get_users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for user in get_users():
        if user[0] == data["username"]:
            return jsonify({"error": "User already exists"}), 400

    add_user(data["username"], data["password"])

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for user in get_users():
        if user[0] == data.get("username") and user[1] == data.get("password"):
            return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": "Invalid credentials"}), 401
