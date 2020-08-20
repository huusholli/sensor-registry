#!/bin/sh

pip install -r requirements.txt

FLASK_APP=sensors \
FLASK_ENV=development \
  flask run \
    --host 0.0.0.0
