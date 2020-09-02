#!/usr/bin/python3
"""Getting started on flask"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Defines response for route '/cities_by_states'"""
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


@app.teardown_appcontext
def teardown(exc):
    """remove the current dbsession"""
    storage.close()

if __name__ == '__main__':
    app.run()
