#!/usr/bin/python3
""" start web flASK"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state():
    """ display state"""
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>")
def city_id(id=None):
    """states + id"""
    states = storage.all('State')
    key = "State.{}".formate(id)
    if key in states:
        city = states[key]
    else:
        city = None
    return render_template('9-states.html', city=city, id=id)


@app.teardown_appcontext
def teardown(exception):
    """ Remove SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
