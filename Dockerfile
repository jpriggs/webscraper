FROM python:3.10.4-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./python-tools /python-tools
RUN pip install -e /python-tools
COPY . /app
