from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/users")
def users():
    return render_template("users.html")

@app.route("/api/users")
def api_users():
    return {
        "users": [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "David"}
        ]
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
