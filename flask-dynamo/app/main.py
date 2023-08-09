from flask import Blueprint, request, jsonify
from botocore.exceptions import BotoCoreError, ClientError
from boto3.dynamodb.conditions import Key
import boto3
import os

def get_dynamodb():
    if os.environ.get('STAGE') == 'compose':
        endpoint_url = 'http://dynamodb-local:8000'
    else:
        endpoint_url = 'http://localhost:8000'

    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
    return boto3.resource(
        'dynamodb',
        region_name='local',
        endpoint_url=endpoint_url,
        aws_access_key_id='dummy',
        aws_secret_access_key='dummy' 
    )

dynamo = get_dynamodb()
example_table = dynamo.Table('ExampleTable')
main = Blueprint('main', __name__)

@main.route('/dynamo/put', methods=['PUT'])
def dynamo_put():
    try:
        data = request.get_json()  # get data from POST request

        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        # put item in DynamoDB table
        response = example_table.put_item(
            Item=data
        )

        # if the put was successful, return success message
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {
                'message': 'Item added successfully',
                'item': {
                    'ExampleTableID': data['ExampleTableID']
                }
            }, 200
        else:
            return jsonify({"error": "Failed to put item into DynamoDB"}), 500

    except (BotoCoreError, ClientError) as error:
        # if there's an error while putting the item in the table, return error message
        return {
            'error': str(error)
        }, 500

    except Exception as error:
        # if there's an error not caught by the above, return error message
        return {
            'error': str(error)
        }, 500

@main.route('/dynamo/query', methods=['POST'])
def dynamo_query():
    try:
        data = request.get_json()  # get data from POST request

        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        # Get item in using query
        response = example_table.query(
            KeyConditionExpression=Key(data["query_key"]).eq(data["query_equals"])
        )

        items = response['Items']

        # if the put was successful, return success message
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {
                'message': 'Items found',
                'item': items
            }, 200
        else:
            return jsonify({"error": "Failed to put item into DynamoDB"}), 500

    except (BotoCoreError, ClientError) as error:
        # if there's an error while putting the item in the table, return error message
        return {
            'error': str(error)
        }, 500

    except Exception as error:
        # if there's an error not caught by the above, return error message
        return {
            'error': str(error)
        }, 500