#!/usr/bin/python3
"""Start a basic Flask web application with 3 route"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Hello route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Adding a specific route /hbnb"""
    return 'HBNB'


@app.route('/c/<string:text>')
def text(text=None):
    """Dynamic inputed text: replace _ for space and show value of text"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
