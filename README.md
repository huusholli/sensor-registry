# SENSOR-REGISTRY

Internal sensor registry to keep track of all kinds of sensors located in `huusholli`.

## Installation

Start application development container with `docker-compose`. API is exposed at http://localhost:5000. Application data is stored at the project root in file `database.json`.

```
docker-compose up
```

## Development

### Running tests

```
python -W ignore::DeprecationWarning -m pytest -s
```

# License

MIT
