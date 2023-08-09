# Flask Microservice
A simple Flask API that is deployed via Docker.

## Development
Use bin commands for shortcuts of the following.
### asdf
Use asdf to manage the python version:
```bash
asdf current python
> python 3.11.3 .../flask-docker/.tool-versions
```
### Pyenv
Use a new pyenv to manage dependencies:
```bash
python -m venv env && source env/bin/activate && pip install -r requirements.txt
which python
> .../flask-docker/env/bin/python
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
docker build -f Dockerfile.dev -t python_flask_docker_service:dev .
```
Run the docker image:
```bash
docker run -dp 5000:5000 python_flask_docker_service:dev
```
Test your endpoint:
```bash
curl --request GET \
  --url http://localhost:5000/ping
```