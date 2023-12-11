from flask import Flask, request, make_response, jsonify
import requests, os
from requests.exceptions import ConnectionError, HTTPError
from datetime import datetime

app = Flask(__name__, instance_relative_config=True)


LOG_URL = 'http://log-service:5000'

def create_app():
    return app

@app.route('/concat')
def concat():
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    if a and b:
        return make_response(jsonify(s=a+b), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

@app.route('/upper')
def upper():
    a = request.args.get('a', 0, type=str)
    return make_response(jsonify(s=a.upper()), 200)

@app.route('/lower')
def lower():
    a = request.args.get('a', 0, type=str)
    return make_response(jsonify(s=a.lower()), 200)
