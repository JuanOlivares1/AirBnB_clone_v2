#!/usr/bin/python3
"""getting started on flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Defines response for route '\'"""
    return 'Hello HBNB!'
