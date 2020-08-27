from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from sensors import routers

app = FastAPI()
app.include_router(routers.router)

def openapi():
  if app.openapi_schema:
    return app.openapi_schema

  openapi_schema = get_openapi(
    title='Sensor Registry',
    version='0.0.1',
    description='',
    routes=app.routes,
  )

  app.openapi_schema = openapi_schema

  return app.openapi_schema

app.openapi = openapi
