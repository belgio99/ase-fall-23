from flask import Flask, request, make_response, jsonify
from requests.exceptions import ConnectionError, HTTPError
import requests, time, os, threading
from datetime import datetime
import random
import operator
from functools import reduce

LOG_URL = 'http://log-service:5000'

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', 0,type=float)
    b = request.args.get('b', 0,type=float)
    return make_response(jsonify(s=a+b), 200)
    
@app.route('/sub')
def sub():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return make_response(jsonify(s=a-b), 200)

@app.route('/mul')
def mul():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return make_response(jsonify(s=a*b), 200)

@app.route('/div')
def div():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    if b == 0:
        return make_response('Cannot divide by zero\n', 400)
    else:
        return make_response(jsonify(s=a/b), 200)

@app.route('/mod')
def mod():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    if b == 0:
        return make_response('Cannot mod by zero\n', 400)
    else:
        return make_response(jsonify(s=a%b), 200)

@app.route('/random')
def random():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    a = int(a)
    b = int(b)
    value = random.randint(a,b)
    
    return make_response(jsonify(s=value), 200)
   
def create_app():
    return app
