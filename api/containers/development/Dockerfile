FROM python:3.11-bookworm

ENV LANG C.UTF-8

WORKDIR /api

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --upgrade pip \
    && pip install poetry==1.5 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
