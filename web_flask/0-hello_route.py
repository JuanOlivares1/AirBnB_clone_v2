#!/usr/bin/env pyrhon3
"""getting started on flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Defines response for route '\'"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
