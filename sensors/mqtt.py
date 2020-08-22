from flask import g
from flask import current_app

from tinydb import TinyDB

import paho.mqtt.client as mqtt

def get_mqtt():
  mqtt_host = current_app.config['MQTT_HOST']

  # Can be None for testing purposes
  if mqtt_host is None:
    return None

  if 'mqtt' not in g:
    g.mqtt = mqtt.Client()
    g.mqtt.connect(current_app.config['MQTT_HOST'])

  return g.mqtt

def publish(topic, value):
  client = get_mqtt()

  if client is not None:
    client.publish(topic, value)
