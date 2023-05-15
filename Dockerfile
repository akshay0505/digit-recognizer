FROM ubuntu:16.04
RUN apt-get update
FROM python:3.9
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["python","api.py"]