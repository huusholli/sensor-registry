import os

from flask import Flask
from flask import json
from werkzeug.exceptions import HTTPException

from sensors.controllers import sensors, health

app = Flask(__name__)

app.config['DATABASE'] = os.path.join(app.root_path, '../database.json')

app.register_blueprint(sensors.api)
app.register_blueprint(health.api)

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()

    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'description': e.description,
    })
    response.content_type = 'application/json'

    return response
