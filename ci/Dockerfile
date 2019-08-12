FROM ubuntu:latest

USER root
WORKDIR /home/scimmia
RUN apt-get update && apt-get install -y \
  redis-tools

COPY test.sh /home/scimmia/