import pytest
from math_py import app

def test_concat(client):
    rv = client.get('/concat?a=ciao&b=pippo')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 'ciaopippo'}

def test_upper(client):
    rv = client.get('/upper?a=prova')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 'PROVA'}

def test_lower(client):
    rv = client.get('/lower?a=PROVA')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 'prova'}