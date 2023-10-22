#!/usr/bin/python3
""" start web flASK"""
from flask import Flask, render_template
app = Flask(__name__)


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


@airbnb.route("/python", strict_slashes=False)
@airbnb.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display message pass when python is called"""
    return "Python " + text.replace("_", " ")


@airbnb.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display n pass when number if it integer"""
    return "{} is a number".format(n)


@airbnb.route("/number_template/<int:n>", strict_slashes=False)
def n(n):
    """display html if n integer"""
    return render_template("5-number.html", n=n)


@airbnb.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """display html if n integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
