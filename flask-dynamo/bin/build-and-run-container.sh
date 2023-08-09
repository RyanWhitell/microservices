#!/bin/bash

docker-compose down service-node
docker-compose build service-node
bin/clean-app.sh
bin/build-app.sh
bin/run-container.sh