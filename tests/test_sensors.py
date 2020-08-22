import pytest
import tempfile
import os

from flask import json
from sensors import app

@pytest.fixture
def client():
  app.config['TESTING'] = True
  app.config['DATABASE'] = tempfile.mkstemp()[1]
  app.config['MQTT_HOST'] = None

  with app.test_client() as client:
    yield client

def test_health(client):
  assert b'OK' in client.get('/health').data

def test_empty_db(client):
  assert len(client.get('/sensors').get_json()) == 0

def test_register_sensor(client):
  sensor = client.post('/sensors', json={
    'type': 'humidity',
    'group': 'ruuvi-mac',
    'offlineTimeout': 20,
  }).get_json()

  assert sensor['id'] != None
  assert sensor['type'] == 'humidity'
  assert sensor['group'] == 'ruuvi-mac'
  assert sensor['createdAt'] != None
  assert sensor['mqttTopic'] == 'sensors/' + sensor['id']

  assert client.get('/sensors/' + sensor['id']).get_json().get('id') == sensor.get('id')
  assert len(client.get('/sensors').get_json()) == 1

def test_remove_sensor(client):
  sensor = client.post('/sensors', json={
    'type': 'humidity',
    'group': 'ruuvi-mac',
    'offlineTimeout': 20,
  }).get_json()

  assert client.delete('/sensors/' + sensor['id']).get_json().get('id') == sensor.get('id')
  assert len(client.get('/sensors').get_json()) == 0

def test_receive_sensor_data(client):
  sensor = client.post('/sensors', json={
    'type': 'pressure',
    'offlineTimeout': 10
  }).get_json()

  assert client.post('/sensors/' + sensor['id'] + '/data', json={
    'value': 10
  }).status_code == 201

  sensor = client.get('/sensors/' + sensor['id']).get_json()

  assert sensor['dataLastReceivedAt'] != None

def test_errorcodes(client):
  assert client.get('/sensors/foo').status_code == 404
  assert client.post('/sensors').status_code == 400
  assert client.delete('/sensors/foo').status_code == 404
  assert client.post('/sensors/foo/data').status_code == 400
