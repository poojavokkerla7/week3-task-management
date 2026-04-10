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
