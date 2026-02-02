"""Pytest configuration"""
import pytest
from app import create_app
from app.config import TestingConfig

"""Pytest configuration"""
import pytest
from app import create_app
from app.config import TestingConfig

@pytest.fixture
def app(mocker):
    """Create application for testing"""
    # Mock database initialization
    mocker.patch('app.models.Database.initialize')
    
    app = create_app(TestingConfig)
    
    yield app

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def sample_task():
    """Create a sample task for testing"""
    return {
        'id': '507f1f77bcf86cd799439011',
        'title': 'Sample Task',
        'description': 'Sample Description',
        'completed': False,
        'created_at': '2023-01-01T00:00:00Z',
        'updated_at': '2023-01-01T00:00:00Z'
    }
