FROM ubuntu:latest

USER root
WORKDIR /home/scimmia
RUN apt-get update && apt-get install -y \
  redis-tools python3.6 python-pip && \
  pip3 install nose && \
  pip3 install redis

COPY scimmia /home/