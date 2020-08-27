from typing import Optional, Dict
from pydantic import BaseModel, Field

from .hash import create_hash
from .utils import PropertyBaseModel

class Sample(BaseModel):
  name: str = Field(..., description='Property name', example='temperature')
  value: float = Field(..., description='Property value', example=12.4)

class Sensor(PropertyBaseModel):
  id: str = Field(default_factory=create_hash)
  device_id: str = Field(description='Unique device ID', example='RuuviTag bu8dw2')
  samples: int = Field(default=0, example=11928, description='Total count of samples posted for this sensor')
  mqtt_topics: Dict[str, str] = Field(default={}, description='Mapping of MQTT topics related to this sensor', example={'temperature': 'sensors/f1qst/temperature'})

  def add_sample(self, sample: Sample):
    self.samples += 1
    self.mqtt_topics[sample.name] = 'sensors/{}/{}'.format(self.id, sample.name)

  @staticmethod
  def from_device(device_id):
    return Sensor(**{'device_id': device_id})
