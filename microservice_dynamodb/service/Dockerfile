FROM python:3.11.3-slim-buster

WORKDIR /app

COPY manage.py manage.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app /app/app

ENV FLASK_APP=routes.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=8080
ENV STAGE=Production

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "manage:app"]
