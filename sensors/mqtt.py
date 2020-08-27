import os
import paho.mqtt.client as mqtt

def get_mqtt():
  mqtt_host = os.environ.get('MQTT_HOST')

  if mqtt_host is None:
    return None

  client = mqtt.Client()
  client.connect(mqtt_host)

  return client

def publish(topic, message):
  client = get_mqtt()

  # May happen in testing for example
  if client is None:
    return

  client.publish(topic, message)
