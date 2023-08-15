import pytest
from app import create_app
from unittest.mock import MagicMock, patch

@pytest.fixture
def app():
    app = create_app(redis_client=MagicMock())
    return app

def test_redis_put(app, mocker):
    mock_set = mocker.patch.object(app.redis_client, 'set', return_value=True)
    
    test_client = app.test_client()
    response = test_client.put("/redis", query_string={"key": "test_key", "value": "test_value"})
    
    assert response.status_code == 200
    assert response.get_json()["message"] == "Data stored successfully"
    
    mock_set.assert_called_once_with("test_key", "test_value")

def test_redis_get(app, mocker):
    mocker.patch.object(app.redis_client, 'exists', return_value=True)
    mock_get = mocker.patch.object(app.redis_client, 'get', return_value=b"test_value")
    
    test_client = app.test_client()
    response = test_client.get("/redis/test_key")
    
    assert response.status_code == 200
    assert response.get_json() == {"key": "test_key", "value": "test_value"}
    
    mock_get.assert_called_once_with("test_key")

def test_redis_get_no_key(app, mocker):
    mocker.patch.object(app.redis_client, 'exists', return_value=False)
    
    test_client = app.test_client()
    response = test_client.get("/redis/test_key")
    
    assert response.status_code == 404
    assert response.get_json() == {"error": "test_key does not exist in Redis"}
