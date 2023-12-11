import pytest
from math_py import app

def test_add(client):
    rv = client.get('/add?a=10&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 13}