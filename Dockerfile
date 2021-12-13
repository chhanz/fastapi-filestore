FROM python:3.10.1-alpine3.15
MAINTAINER han0495@gmail.com

ENV FILESTORE_ID="root" \
    FILESTORE_PASS="testtest"

WORKDIR /usr/src/app

COPY . .
RUN mkdir /usr/src/app/upload \
    && pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9090" ]
