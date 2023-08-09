# Microservice DynamoDB
A simple Flask API that uses DynamoDB as a database.

## Development
Use bin commands for shortcuts of the following.
### asdf
Use asdf to manage the python version:
```bash
asdf current python
> python 3.11.3 .../flask-dynamo/.tool-versions
```
### Pyenv
Use a new pyenv to manage dependencies:
```bash
pyenv-new && pyenv-activate && pyenv-install-reqs
which python
> .../flask-dynamo/env/bin/python
```
### Flask
Run flask locally in debug mode:
```bash
python -m flask run --debug
```
Test your endpoint:
```bash
curl --request GET \
  --url http://127.0.0.1:5000/ping
```
### Docker
Build the docker image:
```bash
docker build -f Dockerfile.dev -t flask_dynamo:dev .
```
Run the docker image:
```bash
docker run -dp 5000:5000 flask_dynamo:dev
```
Test your endpoint:
```bash
curl --request GET \
  --url http://localhost:5000/ping
```
### Docker Compose
Build the service and local dynamodb:
```bash
docker-compose up
```
### Dynamo
Create a table:
```bash
aws dynamodb create-table \
    --table-name <<Table Name>> \
    --attribute-definitions \
        AttributeName=,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Id,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD \
    --endpoint-url http://localhost:8000
```
List tables:
```bash
aws dynamodb list-tables --endpoint-url http://localhost:8000
```