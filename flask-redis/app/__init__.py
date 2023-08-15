from flask import Flask
from .health import health
from .main import main
import redis

def create_app(redis_client=None):
    app = Flask(__name__)

    if not redis_client:
        REDIS_HOST = 'localhost'
        REDIS_PORT = 6379
        REDIS_DB = 0
        redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    app.redis_client = redis_client

    app.register_blueprint(health)
    app.register_blueprint(main)

    return app