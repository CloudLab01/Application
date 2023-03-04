"""
This module defines a simple Flask application.
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    """
    This function returns a simple greeting message
    """
    return "Hello World!"

@app.route("/hello", methods=["GET", "POST"])
def hello_name():
    """
    This function returns a personalized greeting message
    """
    if request.method == "POST" and "name" in request.form:
        name = request.form["name"]
        message = f"Hello {name}!"
        return render_template("hello.html", message=message)
    return render_template("hello.html")


if __name__ == "__main__":
    app.run(debug=True)
