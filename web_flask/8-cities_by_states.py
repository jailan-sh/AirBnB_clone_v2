#!/usr/bin/python3
""" start web flASK"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_list():
    """display cities in state in HTML"""
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Remove SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
