FROM ubuntu:latest

USER root
WORKDIR /home/scimmia
RUN apt-get update && apt-get install -y \
  redis-tools python3.6 python-pip && \
  pip install nose && \
  pip install redis

COPY scimmia /home/scimmia