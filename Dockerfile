
FROM python:3.8

USER root
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
