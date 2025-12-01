FROM ubuntu:latest

ENV VERSION=1.2.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 zip unzip

COPY zip_job.py /tmp/zip_job.py

CMD ["sh", "-c", "uname -a && test -f /tmp/zip_job.py && echo 'zip_job.py exists'"]
