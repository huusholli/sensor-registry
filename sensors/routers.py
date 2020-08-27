import time

from fastapi import APIRouter, Depends, HTTPException, Body, Header, BackgroundTasks, Response
from typing import List
from paho.mqtt.client import Client
from fastapi.responses import StreamingResponse
from paho.mqtt import subscribe

from .models import Sensor, Sample
from .repository import SensorRepository, get_repository
from .hash import create_hash
from .mqtt import publish as mqtt_publish

router = APIRouter()

@router.post('/', status_code=202)
def post_sensor_data(
  body: List[Sample],
  tasks: BackgroundTasks,
  response: Response,
  x_device_id: str = Header(None, description='Sensor\'s unique ID'),
  repository: SensorRepository = Depends(get_repository)
):
  if x_device_id == None:
    raise HTTPException(400, detail='Missing required header X-DEVICE-ID')

  sensor = repository.get_by_device_id(x_device_id) or repository.add(Sensor.from_device(x_device_id))

  for value in body:
    tasks.add_task(mqtt_publish, 'sensors/{}/{}'.format(sensor.id, value.name), value.value)

  response.headers['x-channel-id'] = sensor.id

  return body

