from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

class RegisterSensorInputs(Inputs):
  json = [JsonSchema(schema={
  'type': 'object',
  'properties': {
    'type': {'type': 'string'},
    'group': {'type': 'string'}
  },
  'additionalProperties': False,
  'required': ['type']
})]
