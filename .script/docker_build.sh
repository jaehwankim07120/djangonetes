#!/bin/bash

# build Dockerfile
docker build -t djangonetes-dev . -f Dockerfile.dev
docker build -t djangonetes-live . -f Dockerfile.live