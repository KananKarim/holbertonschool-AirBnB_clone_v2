#!/usr/bin/python3
"""Module that starts a Flask web application:"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Hello method """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return Hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """ Return text """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", strict_slashes=False, defaults={"text": "is_cool"})
@app.route("/python/<text>", strict_slashes=False)
def text_python(text):
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
