from flask import Blueprint, jsonify

health = Blueprint('health', __name__)

@health.route('/ping', methods=['GET'])
def ping():
    return jsonify(message=f'Healthy'), 200

