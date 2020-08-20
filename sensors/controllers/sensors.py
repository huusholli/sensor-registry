from uuid import uuid4

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import abort
from tinydb import TinyDB, Query

from sensors.db import get_db
from sensors.inputs import RegisterSensorInputs

api = Blueprint('sensor_actions', __name__)

@api.route('/sensors', methods=['GET'])
def get_sensors():
  db = get_db()

  return jsonify(db.table('sensors').all())

@api.route('/sensors', methods=['POST'])
def register_sensor():
  if not RegisterSensorInputs(request).validate():
    abort(400)

  db = get_db()
  data = request.json

  id = str(uuid4())

  record = {'id': id, **data}
  db.table('sensors').insert(record)

  return record

@api.route('/sensors/<uuid>', methods=['GET'])
def get_sensor(uuid):
  db = get_db()

  Sensor = Query()

  return db.table('sensors').get(Sensor.id == uuid) or abort(404)

@api.route('/sensors/<uuid>', methods=['DELETE'])
def remove_sensor(uuid):
  db = get_db()
  Sensor = Query()

  record = db.table('sensors').get(Sensor.id == uuid) or abort(404)
  db.table('sensors').remove(Sensor.id == uuid)

  return record
