#!/usr/bin/python3
"""Getting started on flask"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Defines response for route '/states_list'"""
    states=storage.all(State)
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def teardown(exc):
    """remove the current dbsession"""
    storage.close()

if __name__ == '__main__':
    app.run()
