"""Flask application factory"""
from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.routes import api_bp

def create_app(config_class=Config):
    """Create and configure Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    # Serve static files
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    
    return app