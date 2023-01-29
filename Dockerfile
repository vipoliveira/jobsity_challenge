FROM docker.io/python:3.10.9-alpine

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./app ./app
COPY ./.env ./.env
COPY ./secrets ./secrets

ENTRYPOINT [ "uvicorn", "app.main:app" ]
