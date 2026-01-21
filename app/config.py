"""Application configuration"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://mongodb:27017/taskdb')
    MONGO_CONNECT_TIMEOUT = 5000
    MONGO_SERVER_SELECTION_TIMEOUT = 5000

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://mongodb:27017/taskdb_test')

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False