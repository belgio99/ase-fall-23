import requests,time

from flask import Flask, request, make_response
from requests.exceptions import ConnectionError, HTTPError
from urls import *

ALLOWED_MATH_OPS = ['add', 'sub', 'mul', 'div', 'mod', 'random']
ALLOWED_STR_OPS = ['lower', 'upper', 'concat']

app = Flask(__name__, instance_relative_config=True)


def create_app():
    return app

@app.route('/math/<op>')
def math(op):
    if op not in ALLOWED_MATH_OPS:
        return make_response('Invalid operation\n', 404)
    try:
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)
        URL = MATH_URL + f'/{op}?a={a}&b={b}'
        x = requests.get(URL, timeout=1)
        x.raise_for_status()
        res = x.json()
        return res
    except (ConnectionError):
        try:
            URL = MATH_URL + f'/{op}?a={a}&b={b}'
            x = requests.get(URL, timeout=1)
            x.raise_for_status()
            res = x.json()
        except ConnectionError:
            return make_response('Math service is down\n', 404)
        except HTTPError:
            return make_response('Invalid input\n', 400)

        return res

@app.route('/str/<op>')
def string(op):
    if op not in ALLOWED_STR_OPS:
        return make_response('Invalid operation\n', 404)
    try:
        if op == 'lower' or op == 'upper':
           a = request.args.get('a', type=str)
           x = requests.get(STRING_URL + f'/{op}?a={a}', timeout=1)
        else:
            a = request.args.get('a', type=str)
            b = request.args.get('b', type=str)
            x = requests.get(STRING_URL + f'/{op}?a={a}&b={b}', timeout=1)
            time.sleep(1)
        x.raise_for_status()
        return x.json()
    except ConnectionError:
        return make_response('String service is down\n', 404)
    except HTTPError:
        return make_response('Invalid input\n', 400)