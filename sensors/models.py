from typing import Optional
from pydantic import BaseModel, Field

from .hash import create_hash

class Sensor(BaseModel):
  id: str = Field(default_factory=create_hash)
  device_id: str

  @staticmethod
  def from_device(device_id):
    return Sensor(**{'device_id': device_id})

class Sample(BaseModel):
  name: str = Field(..., description='Property name', example='temperature')
  value: float = Field(..., description='Property value', example=12.4)
