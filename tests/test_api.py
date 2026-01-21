"""API unit tests"""
import pytest
import json

def test_create_task(client):
    """Test creating a task"""
    response = client.post('/api/tasks', 
        data=json.dumps({'title': 'Test Task', 'description': 'Test Description'}),
        content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['data']['title'] == 'Test Task'

def test_get_tasks(client):
    """Test getting all tasks"""
    response = client.get('/api/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert 'data' in data

def test_get_task_by_id(client, sample_task):
    """Test getting task by ID"""
    response = client.get(f'/api/tasks/{sample_task["id"]}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['data']['id'] == sample_task['id']

def test_update_task(client, sample_task):
    """Test updating a task"""
    response = client.put(f'/api/tasks/{sample_task["id"]}',
        data=json.dumps({'title': 'Updated Task', 'completed': True}),
        content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['data']['title'] == 'Updated Task'
    assert data['data']['completed'] == True

def test_delete_task(client, sample_task):
    """Test deleting a task"""
    response = client.delete(f'/api/tasks/{sample_task["id"]}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True

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