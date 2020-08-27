FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip install --no-cache-dir uvicorn \
    && apk del .build-deps gcc libc-dev make

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]
