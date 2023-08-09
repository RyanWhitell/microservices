import pytest
from flask import Flask
from app import main, create_app
from unittest.mock import MagicMock

@pytest.fixture
def app():
    app = create_app()
    return app

def test_dynamo_put(app, mocker):
    # Mocking the DynamoDB table
    example_table_mock = MagicMock()
    example_table_mock.put_item.return_value = {
        'ResponseMetadata': {'HTTPStatusCode': 200}
    }

    mocker.patch('app.main.example_table', example_table_mock)

    # Creating payload
    payload = {
        "ExampleTableID": "123"
    }

    test_client = app.test_client()
    response = test_client.put('/dynamo/put', json=payload)

    assert response.status_code == 200
    assert response.json['message'] == 'Item added successfully'
    assert response.json['item']['ExampleTableID'] == payload['ExampleTableID']

def test_dynamo_query(app, mocker):
    # Mocking the DynamoDB table
    example_table_mock = MagicMock()
    example_table_mock.query.return_value = {
        'ResponseMetadata': {'HTTPStatusCode': 200},
        'Items': [{'key': 'value'}]
    }

    mocker.patch('app.main.example_table', example_table_mock)

    # Creating payload
    payload = {
        "query_key": "key",
        "query_equals": "value"
    }

    test_client = app.test_client()
    response = test_client.post('/dynamo/query', json=payload)

    assert response.status_code == 200
    assert response.json['message'] == 'Items found'
    assert response.json['item'][0]['key'] == payload['query_equals']
