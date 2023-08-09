# Flask API
A simple Flask API.

## Development
Use bin commands for shortcuts of the following.
### asdf
Use asdf to manage the python version:
```bash
asdf current python
> python 3.11.3 .../flask-api/.tool-versions
```
### Pyenv
Use a new pyenv to manage dependencies:
```bash
python -m venv env && source env/bin/activate && pip install -r requirements.txt
which python
> .../flask-api/env/bin/python
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