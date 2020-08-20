FROM python:3.8-alpine

RUN apk --update add git

WORKDIR /app

COPY . .

ENTRYPOINT ["sh", "docker-entrypoint-dev.sh"]
