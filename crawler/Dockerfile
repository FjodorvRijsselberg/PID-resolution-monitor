FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR root
COPY crawler/pyproject.toml .
RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR src
COPY crawler/ .
COPY pyproject.toml ./stub.toml

RUN poetry install
