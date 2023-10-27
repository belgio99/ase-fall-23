from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)

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
def mul():
    a = request.args.get('a', 0, type=str)
    return make_response(jsonify(s=a.lower()), 200)


def create_app():
    return app