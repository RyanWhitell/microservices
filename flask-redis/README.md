# Microservice Redis
A simple Flask API that uses Redis as a key-value store and cache.

## Development
Use bin commands for shortcuts of the following.
### asdf
Use asdf to manage the python version:
```bash
asdf current python
> python 3.11.3 .../flask-redis/.tool-versions
```
### Pyenv
Use a new pyenv to manage dependencies:
```bash
pyenv-new && pyenv-activate && pyenv-install-reqs
which python
> .../flask-redis/env/bin/python
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
docker build -f Dockerfile.dev -t flask_redis:dev .
```
Run the docker image:
```bash
docker run -dp 5000:5000 flask_redis:dev
```
Test your endpoint:
```bash
curl --request GET \
  --url http://localhost:5000/ping
```
### Docker Compose
Build the service and local redis:
```bash
docker-compose up
```
### Redis