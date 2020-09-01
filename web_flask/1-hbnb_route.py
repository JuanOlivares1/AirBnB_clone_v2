#!/usr/bin/python3
"""Getting started on flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Defines response for route '/'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Defines response for route '/hbnb'"""
    return 'HBNB'

if __name__ == '__main__':
    app.run()
