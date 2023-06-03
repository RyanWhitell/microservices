from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/ping/<string:name>', methods=['GET'])
def ping(name: str):
    if 'name' in request.args:
        name = request.args.get('name')
    return jsonify(message=f'Pong! Hello {name}'), 200

@main.route('/health', methods=['GET', 'PUT', 'POST', 'DELETE'])
def health():
    return jsonify(message='Healthy'), 200