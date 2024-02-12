FROM ubuntu


# Use an official Python runtime as a parent image
FROM python:3.9-slim

COPY . /pytest-api-gorest
WORKDIR /pytest-api-gorest

RUN pip install --no-cache-dir -r requirements.txt
CMD pytest ./tests_users.py ./tests_posts.py --junitxml=/pytest-api-gorest/result.xml
