FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make git \
    && pip install --no-cache-dir uvicorn \
    && apk del .build-deps gcc libc-dev make

WORKDIR /app

COPY . .

ENTRYPOINT ["sh", "docker-entrypoint-dev.sh"]
