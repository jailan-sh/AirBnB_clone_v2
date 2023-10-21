#!/usr/bin/python3
""" start web flASK"""


from flask import Flask


airbnb = Flask(__name__)


@airbnb.route("/", strict_slashes=False)
def hello():
    """display hello"""
    return "Hello HBNB!"


@airbnb.route("/hbnb", strict_slashes=False)
def about_hbnb():
    """display hbnb"""
    return "HBNB"


@airbnb.route("/c/<text>", strict_slashes=False)
def fun_c(text):
    """display message pass when c is called"""
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    airbnb.run(host="0.0.0.0", port=5000, debug=True)
