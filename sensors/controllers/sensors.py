from uuid import uuid4
from datetime import datetime
from datetime import timedelta

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import abort
from tinydb import TinyDB, Query

from sensors.db import get_db
from sensors.mqtt import publish
from sensors.inputs import RegisterSensorInputs
from sensors.inputs import ReceiveSensorDataInput

api = Blueprint('sensor_actions', __name__)

def format_sensor(sensor):
  is_online = False

  if sensor.get('dataLastReceivedAt') != None:
    time_last_receive = datetime.strptime(sensor['dataLastReceivedAt'], '%Y-%m-%d %H:%M:%S.%f')
    time_now = datetime.now()
    is_online = (time_now - time_last_receive).seconds < int(sensor.get('offlineTimeout'))

  return {
    **sensor,
    'isOnline': is_online,
    'mqttTopic': 'sensors/' + sensor.get('id')
  }

@api.route('/sensors', methods=['GET'])
def get_sensors():
  db = get_db()

  sensors = db.table('sensors').all()

  return jsonify(list(map(format_sensor, sensors)))

@api.route('/sensors', methods=['POST'])
def register_sensor():
  if not RegisterSensorInputs(request).validate():
    abort(400)

  db = get_db()
  data = request.json

  id = str(uuid4())

  record = {
    'id': id,
    'createdAt': str(datetime.now()),
    **data
  }

  db.table('sensors').insert(record)

  return format_sensor(record), 201

@api.route('/sensors/<uuid>', methods=['GET'])
def get_sensor(uuid):
  db = get_db()

  Sensor = Query()

  sensor = db.table('sensors').get(Sensor.id == uuid) or abort(404)

  return format_sensor(sensor)

@api.route('/sensors/<uuid>', methods=['DELETE'])
def remove_sensor(uuid):
  db = get_db()
  Sensor = Query()

  record = db.table('sensors').get(Sensor.id == uuid) or abort(404)
  db.table('sensors').remove(Sensor.id == uuid)

  return record

@api.route('/sensors/<uuid>/data', methods=['POST'])
def receive_data(uuid):
  if not ReceiveSensorDataInput(request).validate():
    abort(400)

  db = get_db()
  Sensor = Query()

  record = db.table('sensors').get(Sensor.id == uuid) or abort(404)

  record['dataLastReceivedAt'] = str(datetime.now())

  db.table('sensors').update(record, Sensor.id == uuid)
  publish('sensors/' + uuid, request.json.get('value'))

  return record, 201

