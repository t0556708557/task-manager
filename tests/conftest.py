"""Pytest configuration"""
import pytest
from app import create_app
from app.config import TestingConfig
from app.models import Database
import json

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app(TestingConfig)
    
    with app.app_context():
        Database.initialize()
        # Clear test database
        Database.db.tasks.delete_many({})
    
    yield app
    
    # Cleanup
    with app.app_context():
        Database.db.tasks.delete_many({})

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def sample_task(client):
    """Create a sample task for testing"""
    response = client.post('/api/tasks',
        data=json.dumps({
            'title': 'Sample Task',
            'description': 'Sample Description',
            'completed': False
        }),
        content_type='application/json')
    
    return json.loads(response.data)['data']