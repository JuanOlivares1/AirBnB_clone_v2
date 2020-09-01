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


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Defines response for route '/c/<text>'"""
    return "C " + " ".join(text.split('_'))


if __name__ == '__main__':
    app.run()
