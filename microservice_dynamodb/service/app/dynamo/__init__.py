import boto3
import os

def get_dynamodb():
    if os.environ.get('STAGE') == 'Production':
        return boto3.resource('dynamodb', region_name='us-west-2')
    else:
        return boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')

dynamo = get_dynamodb()
example_table = dynamo.Table('ExampleTable')

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html