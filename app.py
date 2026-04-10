from flask import Flask, render_template
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

# Create Flask app
app = Flask(__name__)

# Secret key (used for sessions/security basics)
app.secret_key = "secret123"

# Register routes (connect files)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

@app.route("/")
def home():
    return render_template("index.html")
# Run the app
if __name__ == "__main__":
    app.run(debug=True)
