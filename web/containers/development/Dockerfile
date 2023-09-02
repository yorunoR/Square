FROM node:18.17-bookworm-slim

WORKDIR /web

COPY package.json /web/package.json

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
