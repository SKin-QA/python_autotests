import requests
import pytest

host = 'https://pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_string_in_body():
    response = requests.get (f'{host}/trainers', params={'trainer_id': '4649'})
    assert response.json()['trainer_name'] == 'Lana'