import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_health_check(app):
    test_client = app.test_client()
    response = test_client.get('/ping')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Healthy'