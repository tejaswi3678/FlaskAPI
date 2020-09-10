# importing packages
import flask
import json
import requests

from flask import render_template, Flask, jsonify, request

global a, b, data
data = {"def": 1}

app = Flask(__name__)


# operation route add
@app.route('/add', methods=['POST'])
def add():
    # header
    global a, b, data, addition
    content = request.get_json(silent=True)
    data = request.get_json()
    a = data['first']
    b = data['second']
    addition = a + b
    return flask.jsonify(addition)


# operation route subtract
@app.route('/subtract', methods=['POST', 'GET'])
def subtract():
    # header
    global a, b, data, subtraction
    content = request.get_json(silent=True)
    data = request.get_json()
    a = data['first']
    b = data['second']
    subtraction = a - b
    return flask.jsonify(subtraction)


# operation route multiply
@app.route('/multiply', methods=['POST', 'GET'])
def multiply():
    # header
    global a, b, data, multiplication
    content = request.get_json(silent=True)
    data = request.get_json()
    a = data['first']
    b = data['second']
    multiplication = a * b
    return flask.jsonify(multiplication)


# operation route divide
@app.route('/divide', methods=['POST', 'GET'])
def divide():
    # header
    global a, b, data, division
    content = request.get_json(silent=True)
    data = request.get_json()
    a = data['first']
    b = data['second']
    division = a / b
    return flask.jsonify(division)


@app.route("/add/latest", methods=['GET'])
def add_latest():
    if data.get('def'):
        res = {"error": "None addition were made before, go and add something"}
    else:
        res = {"first": a, "second": b, "result": addition}
    return flask.jsonify(res)


@app.route("/subtract/latest", methods=['GET'])
def sub_latest():
    if data.get('def'):
        res = {"error": "None subtractions were made before, go and subtract something"}
    else:
        res = {"first": a, "second": b, "result": subtraction}
    return flask.jsonify(res)


@app.route("/multiply/latest", methods=['GET'])
def mul_latest():
    if data.get('def'):
        res = {"error": "None multiplications were made before, go and multiply something"}
    else:
        res = {"first": a, "second": b, "result": multiplication}
    return flask.jsonify(res)


@app.route("/division/latest", methods=['GET'])
def div_latest():
    if data.get('def'):
        res = {"error": "None divisions were made before, go and divide something"}
    else:
        res = {"first": a, "second": b, "result": division}
    return flask.jsonify(res)


if __name__ == '__main__':
    app.run(port='5002')