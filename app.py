from flask import Flask, redirect, url_for, request, session, flash
from datetime import timedelta

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Testing</h1> <p>isn't this cool?</p>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))    


if __name__ == "__main__":
    app.run(port=8003)