# Microservice DynamoDB
A simple Flask API that is deployed to AWS and uses DynamoDB as a database.

## Development
### asdf
Use asdf to manage the python version:
```bash
asdf current python
> python 3.11.3 .../microservices/microservice-simple/.tool-versions
```
### Pyenv
Use a new pyenv to manage dependencies:
```bash
pyenv-new && pyenv-activate && pyenv-install-reqs
which python
> ...microservices/microservice-simple/python_flask_docker_service/env/bin/python
```
### Flask
Run flask locally in debug mode:
```bash
python -m flask run --debug
```
Test your endpoint:
```bash
curl --request GET \
  --url http://127.0.0.1:5000/ping/ryan
```
### Docker
Build the docker image:
```bash
docker build -t python_flask_docker_service .
```
Run the docker image:
```bash
docker run -dp 5000:5000 python_flask_docker_service
```
Test your endpoint:
```bash
curl --request GET \
  --url http://localhost:5000/ping/dave
```