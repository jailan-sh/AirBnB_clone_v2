#!/usr/bin/python3
""" start web flASK"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardwon(self):
    """ remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def satatic_list():
    """display a HTML page"""
    states = storage.all('State').values()
    states = sorted(states, key=lambda k: k.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
