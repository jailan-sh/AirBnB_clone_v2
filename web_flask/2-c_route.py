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
    """display anther route"""
    return "HBNB"


@airbnb.route("/c/is_fun", strict_slashes=False)
def fun_c():
    """display anther route"""
    return "C is fun"


@airbnb.route("/c/cool", strict_slashes=False)
def cool_c():
    """display anther route"""
    return "C cool"


if __name__ == "__main__":
    airbnb.run(host="0.0.0.0", port=5000, debug=True)
