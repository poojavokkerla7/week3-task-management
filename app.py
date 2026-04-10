from flask import Flask
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

# Create Flask app
app = Flask(__name__)

# Secret key (used for sessions/security basics)
app.secret_key = "secret123"

# Register routes (connect files)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
