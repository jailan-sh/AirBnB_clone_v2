#!/usr/bin/python3
""" start web flASK"""


from flask import Flask


airbnb = Flask(__name__)

@airbnb.route("/", strict_slashes=False)
def hello():
    """display hello"""
    return "Hello HBNB!"

if __name__ == "__main__":
        airbnb.run(host="0.0.0.0", port=5000, debug=True)
