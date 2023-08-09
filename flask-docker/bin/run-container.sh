#!/bin/bash

docker build -f Dockerfile.dev -t python_flask_docker_service:dev .
docker run -dp 5000:5000 python_flask_docker_service:dev
