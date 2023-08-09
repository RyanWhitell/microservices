from flask import Flask
from .health import health

def create_app():
    app = Flask(__name__)

    app.register_blueprint(health)

    return app

