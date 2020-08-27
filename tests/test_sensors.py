import pytest
from tempfile import mkstemp
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

device_a = {'x-device-id': 'Device A'}
device_b = {'x-device-id': 'Device B'}

@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
  monkeypatch.setenv('STORAGE_PATH', mkstemp()[1])

def test_post_no_data():
  assert client.post('/').status_code == 422

def test_post_no_device_id():
  assert client.post('/', json=[]).status_code == 400

def test_post_valid_data():
  data = [{'name': 'temperature', 'value': 12}, {'name': 'humidity', 'value': 57.2}]
  response = client.post('/', json=data, headers=device_a)

  assert response.status_code == 202
  assert response.headers.get('x-channel-id') != None

def test_post_same_device():
  data = []

  channel_1 = client.post('/', json=data, headers=device_a).headers.get('x-channel-id')
  channel_2 =client.post('/', json=data, headers=device_a).headers.get('x-channel-id')

  assert channel_1 == channel_2

def test_post_two_devices():
  data = []

  channel_a = client.post('/', json=data, headers=device_a).headers.get('x-channel-id')
  channel_b = client.post('/', json=data, headers=device_b).headers.get('x-channel-id')

  assert channel_a != channel_b
