"""API routes"""
from flask import Blueprint, request, jsonify
from app.models import Task, Database
import logging

logger = logging.getLogger(__name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.before_app_request
def initialize_database():
    """Initialize database"""
    Database.initialize()

@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        tasks = Task.get_all()
        return jsonify({'success': True, 'data': tasks, 'count': len(tasks)}), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': 'Failed to retrieve tasks'}), 500

@api_bp.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    """Get task by ID"""
    try:
        task = Task.get_by_id(task_id)
        if not task:
            return jsonify({'success': False, 'error': 'Task not found'}), 404
        return jsonify({'success': True, 'data': task}), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': 'Failed to retrieve task'}), 500

@api_bp.route('/tasks', methods=['POST'])
def create_task():
    """Create task"""
    try:
        data = request.get_json()
        if not data or 'title' not in data:
            return jsonify({'success': False, 'error': 'Title required'}), 400
        
        title = data['title'].strip()
        if not title:
            return jsonify({'success': False, 'error': 'Title cannot be empty'}), 400
        
        task = Task.create(
            title=title,
            description=data.get('description', ''),
            completed=data.get('completed', False)
        )
        return jsonify({'success': True, 'data': task, 'message': 'Task created'}), 201
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': 'Failed to create task'}), 500

@api_bp.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    """Update task"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        if 'title' in data:
            title = data['title'].strip()
            if not title:
                return jsonify({'success': False, 'error': 'Title cannot be empty'}), 400
            data['title'] = title
        
        task = Task.update(task_id, **data)
        if not task:
            return jsonify({'success': False, 'error': 'Task not found'}), 404
        
        return jsonify({'success': True, 'data': task, 'message': 'Task updated'}), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': 'Failed to update task'}), 500

@api_bp.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete task"""
    try:
        success = Task.delete(task_id)
        if not success:
            return jsonify({'success': False, 'error': 'Task not found'}), 404
        return jsonify({'success': True, 'message': 'Task deleted'}), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': 'Failed to delete task'}), 500

@api_bp.route('/tasks/completed', methods=['DELETE'])
def delete_completed():
    """Delete completed tasks"""
    try:
        count = Task.delete_completed()
        return jsonify({'success': True, 'message': f'Deleted {count} tasks', 'count': count}), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': 'Failed to delete completed tasks'}), 500

@api_bp.route('/tasks/search', methods=['GET'])
def search_tasks():
    """Search tasks"""
    try:
        query = request.args.get('q', '').strip()
        if not query:
            return jsonify({'success': False, 'error': 'Search query required'}), 400
        
        tasks = Task.search(query)
        return jsonify({'success': True, 'data': tasks, 'count': len(tasks), 'query': query}), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': 'Failed to search tasks'}), 500