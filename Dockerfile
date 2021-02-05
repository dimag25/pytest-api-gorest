FROM ubuntu
MAINTAINER gurevich89@gmail.com


# Use an official Python runtime as a parent image
FROM python:3.6-slim

COPY . /twtask_python
WORKDIR /twtask_python

RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "test.py", "--junitxml=reports/result.xml"]
