from tinydb import TinyDB, Query

from .models import Sensor

db = TinyDB('data/database.json')

class SensorRepository():
  def add(self, sensor: Sensor):
    db.table('sensors').insert(sensor.dict())
    return sensor

  def get_by_device_id(self, device_id: str):
    sensor = db.table('sensors').get(Query().device_id == device_id)
    return None if sensor is None else Sensor(**sensor)

repository = SensorRepository()

def get_repository():
  return repository
