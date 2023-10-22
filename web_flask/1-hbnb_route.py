#!/usr/bin/python3
""" start web flASK"""


from flask import Flask


app = Flask(__name__)


@airbnb.route("/", strict_slashes=False)
def hello():
    """display hello"""
    return "Hello HBNB!"


@airbnb.route("/hbnb", strict_slashes=False)
def about_hbnb():
    """display anther route"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
