# app/__init__.py
from flask import Flask
from .database import init_db

# Initialize Flask app
app = Flask(__name__)

# Initialize database
init_db()

# Import routes after app initialization to avoid circular imports
from . import routes