"""Database models"""
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from flask import current_app
import logging

logger = logging.getLogger(__name__)

class Database:
    """MongoDB connection manager"""
    client = None
    db = None
    
    @staticmethod
    def initialize():
        """Initialize database connection"""
        try:
            Database.client = MongoClient(
                current_app.config['MONGO_URI'],
                serverSelectionTimeoutMS=current_app.config['MONGO_CONNECT_TIMEOUT']
            )
            db_name = current_app.config['MONGO_URI'].split('/')[-1].split('?')[0]
            Database.db = Database.client[db_name]
            Database.client.server_info()
            logger.info("MongoDB connected")
        except Exception as e:
            logger.error(f"MongoDB connection failed: {str(e)}")
            raise
    
    @staticmethod
    def get_collection(name):
        """Get collection"""
        if Database.db is None:
            Database.initialize()
        return Database.db[name]

class Task:
    """Task model"""
    collection_name = 'tasks'
    
    @staticmethod
    def create(title, description='', completed=False):
        """Create task"""
        collection = Database.get_collection(Task.collection_name)
        task = {
            'title': title,
            'description': description,
            'completed': completed,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        result = collection.insert_one(task)
        task['_id'] = result.inserted_id
        return Task._serialize(task)
    
    @staticmethod
    def get_all():
        """Get all tasks"""
        collection = Database.get_collection(Task.collection_name)
        tasks = list(collection.find().sort('created_at', -1))
        return [Task._serialize(t) for t in tasks]
    
    @staticmethod
    def get_by_id(task_id):
        """Get task by ID"""
        collection = Database.get_collection(Task.collection_name)
        try:
            task = collection.find_one({'_id': ObjectId(task_id)})
            return Task._serialize(task) if task else None
        except:
            return None
    
    @staticmethod
    def update(task_id, **kwargs):
        """Update task"""
        collection = Database.get_collection(Task.collection_name)
        try:
            update_data = {k: v for k, v in kwargs.items() if v is not None}
            update_data['updated_at'] = datetime.utcnow()
            result = collection.update_one(
                {'_id': ObjectId(task_id)},
                {'$set': update_data}
            )
            return Task.get_by_id(task_id) if result.modified_count else None
        except:
            return None
    
    @staticmethod
    def delete(task_id):
        """Delete task"""
        collection = Database.get_collection(Task.collection_name)
        try:
            result = collection.delete_one({'_id': ObjectId(task_id)})
            return result.deleted_count > 0
        except:
            return False
    
    @staticmethod
    def delete_completed():
        """Delete all completed tasks"""
        collection = Database.get_collection(Task.collection_name)
        result = collection.delete_many({'completed': True})
        return result.deleted_count
    
    @staticmethod
    def search(query):
        """Search tasks"""
        collection = Database.get_collection(Task.collection_name)
        tasks = list(collection.find({
            '$or': [
                {'title': {'$regex': query, '$options': 'i'}},
                {'description': {'$regex': query, '$options': 'i'}}
            ]
        }).sort('created_at', -1))
        return [Task._serialize(t) for t in tasks]
    
    @staticmethod
    def _serialize(task):
        """Serialize task to JSON"""
        if not task:
            return None
        return {
            'id': str(task['_id']),
            'title': task['title'],
            'description': task.get('description', ''),
            'completed': task.get('completed', False),
            'created_at': task['created_at'].isoformat() + 'Z',
            'updated_at': task['updated_at'].isoformat() + 'Z'
        }