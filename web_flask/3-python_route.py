#!/usr/bin/python3
"""
Starting a basic flasj  web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """
        Returns a string when queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        Returns a string when queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """
        Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """
        Reformats text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

