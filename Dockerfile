FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app/

ENV TZ=Europe/Amsterdam \
    PYTHONUNBUFFERED='1' \
    APP_MODULE=src.ontogpt_api.main:app \
    MAX_WORKERS='16'

## Check here for more details on how the image is built and which env variables are available
# https://github.com/tiangolo/uvicorn-gunicorn-docker/tree/master/docker-images
#   WORKER_CLASS=uvicorn.workers.UvicornWorker \
#   WORKERS_PER_CORE='1' \
#   LOG_LEVEL=info

RUN apt-get update && \
    apt-get install -y tzdata && \
    pip install --upgrade pip


COPY . /app

RUN pip install .
