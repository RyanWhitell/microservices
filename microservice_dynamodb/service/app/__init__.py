from flask import Flask
from .api.health import health
from .api.main import main

def create_app():
    app = Flask(__name__)

    # Routes
    app.register_blueprint(health)
    app.register_blueprint(main)

    return app