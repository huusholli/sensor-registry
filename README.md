# SENSOR-REGISTRY

[![Actions Status](https://github.com/huusholli/sensor-registry/workflows/CI/badge.svg)](https://github.com/huusholli/sensor-registry/actions)

Internal sensor registry to keep track of all kinds of sensors located in `huusholli`.

## Installation

Start application development container with `docker-compose`. API is exposed at http://localhost:5000. Application data is stored at the project root in file `database.json`.

```
docker-compose up
```

## API Docs

Swagger: http://localhost:5000/docs
Redoc: http://localhost:5000/redoc

## Development

### Running tests

```
pytest
```

# License

MIT
