from os import getenv
from tinydb import TinyDB, Query

from .models import Sensor

class SensorRepository():
  def add(self, sensor: Sensor):
    get_db().table('sensors').insert(sensor.dict())
    return sensor

  def update(self, sensor: Sensor):
    get_db().table('sensors').update(sensor, Query().id == sensor.id)

  def get_by_device_id(self, device_id: str):
    sensor = get_db().table('sensors').get(Query().device_id == device_id)
    return None if sensor is None else Sensor(**sensor)

  def get_all(self):
    format_sensor = lambda sensor : Sensor(**sensor)
    return list(map(format_sensor, get_db().table('sensors').all()))

repository = SensorRepository()

def get_db():
  return TinyDB(getenv('STORAGE_PATH'))

def get_repository():
  return repository
