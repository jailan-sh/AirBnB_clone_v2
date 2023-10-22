#!/usr/bin/python3
""" start web flASK"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def about_hbnb():
    """display hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def fun_c(text):
    """display message pass when c is called"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display message pass when python is called"""
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
