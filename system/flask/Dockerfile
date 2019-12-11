#Pull image for Linux Alpine with Python 3.8
FROM python:3.8.0-alpine
MAINTAINER Janus Bo Andersen

#Set the working directory inside the Alpine Container
WORKDIR /usr/src/flask

#Set environment variables
#don't write .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
#don't buffer stdout, as that causes errors
ENV PYTHONUNBUFFERED 1

#Install dependencies for PostgreSQL (Psycopg2)
RUN apk update && apk add postgresql-dev gcc musl-dev shadow curl

#Install dependencies inside container
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/flask/requirements.txt
RUN pip install -r requirements.txt

#Create a user to avoid running as root.
RUN adduser -D nonrootuser
USER nonrootuser
