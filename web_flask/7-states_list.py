#!/usr/bin/python3
""" start web flASK"""
from flask import Flask, render_template
from models.state import State
from models import storage

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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display n pass when number if it integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n(n):
    """display html if n integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """display html if n integer"""
    return render_template("6-number_odd_or_even.html", n=n)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """states_list."""
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Remove SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
