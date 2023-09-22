#!/usr/bin/python3
"""starts a flask web app"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """prints Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """prints HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def ctext(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<int:n>")
def num(n):
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>")
def numTemp(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def numOddorEven(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
