#!/bin/bash

# run docker-compose
#docker-compose up --build -d

# run Dockerfile
docker build -t djangonetes-dev . -f Dockerfile.dev
docker build -t djangonetes-live . -f Dockerfile.live