"""API unit tests"""
import pytest
import json
from unittest.mock import Mock

def test_create_task(client, mocker):
    """Test creating a task"""
    mock_task = {
        'id': '507f1f77bcf86cd799439011',
        'title': 'Test Task',
        'description': 'Test Description',
        'completed': False,
        'created_at': '2023-01-01T00:00:00Z',
        'updated_at': '2023-01-01T00:00:00Z'
    }
    
    mock_create = mocker.patch('app.models.Task.create', return_value=mock_task)
    
    response = client.post('/api/tasks', 
        data=json.dumps({'title': 'Test Task', 'description': 'Test Description'}),
        content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['data']['title'] == 'Test Task'
    mock_create.assert_called_once_with(
        title='Test Task',
        description='Test Description',
        completed=False
    )

def test_get_tasks(client, mocker):
    """Test getting all tasks"""
    mock_tasks = [
        {
            'id': '507f1f77bcf86cd799439011',
            'title': 'Task 1',
            'description': 'Description 1',
            'completed': False,
            'created_at': '2023-01-01T00:00:00Z',
            'updated_at': '2023-01-01T00:00:00Z'
        }
    ]
    
    mock_get_all = mocker.patch('app.models.Task.get_all', return_value=mock_tasks)
    
    response = client.get('/api/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert 'data' in data
    assert len(data['data']) == 1
    mock_get_all.assert_called_once()

def test_get_task_by_id(client, sample_task, mocker):
    """Test getting task by ID"""
    mock_get_by_id = mocker.patch('app.models.Task.get_by_id', return_value=sample_task)
    
    response = client.get(f'/api/tasks/{sample_task["id"]}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['data']['id'] == sample_task['id']
    mock_get_by_id.assert_called_once_with(sample_task['id'])

def test_update_task(client, sample_task, mocker):
    """Test updating a task"""
    updated_task = sample_task.copy()
    updated_task['title'] = 'Updated Task'
    updated_task['completed'] = True
    updated_task['updated_at'] = '2023-01-02T00:00:00Z'
    
    mock_update = mocker.patch('app.models.Task.update', return_value=updated_task)
    
    response = client.put(f'/api/tasks/{sample_task["id"]}',
        data=json.dumps({'title': 'Updated Task', 'completed': True}),
        content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['data']['title'] == 'Updated Task'
    assert data['data']['completed'] == True
    mock_update.assert_called_once_with(sample_task['id'], title='Updated Task', completed=True)

def test_delete_task(client, sample_task, mocker):
    """Test deleting a task"""
    mock_delete = mocker.patch('app.models.Task.delete', return_value=True)
    
    response = client.delete(f'/api/tasks/{sample_task["id"]}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    mock_delete.assert_called_once_with(sample_task['id'])

def test_search_tasks(client, sample_task):
    """Test searching tasks"""
    response = client.get('/api/tasks/search?q=Sample')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert len(data['data']) > 0

def test_delete_completed_tasks(client):
    """Test deleting completed tasks"""
    # Create completed task
    client.post('/api/tasks',
        data=json.dumps({'title': 'Completed Task', 'completed': True}),
        content_type='application/json')
    
    response = client.delete('/api/tasks/completed')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True

def test_create_task_without_title(client):
    """Test creating task without title"""
    response = client.post('/api/tasks',
        data=json.dumps({'description': 'No title'}),
        content_type='application/json')
    
    assert response.status_code == 400

def test_get_nonexistent_task(client):
    """Test getting non-existent task"""
    response = client.get('/api/tasks/507f1f77bcf86cd799439011')
    assert response.status_code == 404
