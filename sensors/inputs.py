from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

class RegisterSensorInputs(Inputs):
  json = [JsonSchema(schema={
    'type': 'object',
    'properties': {
      'type': {'type': 'string'},
      'group': {'type': 'string'},
      'offlineTimeout': {'type': 'number', 'minimum': 1}
    },
    'additionalProperties': False,
    'required': ['type', 'offlineTimeout']
  })]

class ReceiveSensorDataInput(Inputs):
  json = [JsonSchema(schema={
    'type': 'object',
    'properties': {
      'value': {'type': 'number'}
    },
    'additionalProperties': False,
    'required': ['value']
  })]
