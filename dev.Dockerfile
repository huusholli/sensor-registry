FROM python:3.7.9-alpine

RUN apk --update add git

WORKDIR /app

COPY . .

ENTRYPOINT ["sh", "docker-entrypoint-dev.sh"]
