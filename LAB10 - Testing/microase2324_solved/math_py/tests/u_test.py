import pytest
from math_py import app

def test_add(client):
    rv = client.get('/add?a=10&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 13}

def test_sub(client):
    rv = client.get('/sub?a=10&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 7}

def test_mul(client):
    rv = client.get('/mul?a=10&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 30}

def test_div(client):
    rv = client.get('/div?a=10&b=5')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 2}

def test_div_zero(client):
    rv = client.get('/div?a=10&b=0')
    assert rv.status_code == 400

def test_mod(client):
    rv = client.get('/mod?a=3&b=2')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 1}

def test_mod_zero(client):
    rv = client.get('/mod?a=3&b=0')
    assert rv.status_code == 400

def random(client):
    rv = client.get('/ran?a=10&b=20')
    assert rv.status_code == 200
    json_response = rv.get_json()
    assert json_response['s'] >= 10 and json_response['s'] <= 20
    