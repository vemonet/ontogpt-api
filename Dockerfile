FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
# https://github.com/tiangolo/uvicorn-gunicorn-docker/tree/master/docker-images

WORKDIR /app/

ENV TZ=Europe/Amsterdam \
    PYTHONUNBUFFERED='1' \
    APP_MODULE=src.ontogpt_api.main:app \
    MAX_WORKERS='16'
    # LOG_LEVEL=info

RUN apt-get update && \
    apt-get install -y tzdata && \
    pip install --upgrade pip

COPY . /app

RUN pip install .
