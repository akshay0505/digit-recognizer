FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get python3-opencv libopencv-dev -y
FROM python:3.9
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["python","api.py"]