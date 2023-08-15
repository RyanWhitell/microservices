from flask import Blueprint, jsonify, request, current_app
import redis

main = Blueprint('main', __name__)

@main.route('/redis', methods=['PUT'])
def redis_put():
    try:
        key = request.args.get('key')
        value = request.args.get('value')

        if not key or not value:
            return jsonify({"error": "key and value query parameters are required"}), 400

        current_app.redis_client.set(key, value)
        return jsonify({"message": "Data stored successfully"})

    except redis.RedisError:
        return jsonify({"error": "Failed to store data in Redis"}), 500

@main.route('/redis/<string:key>', methods=['GET'])
def redis_get(key):
    try:
        if current_app.redis_client.exists(key):
            return jsonify({"key": key, "value": current_app.redis_client.get(key).decode('utf-8')})
        else:
            return jsonify({"error": f"{key} does not exist in Redis"}), 404

    except redis.RedisError:
        return jsonify({"error": "Failed to retrieve data from Redis"}), 500
