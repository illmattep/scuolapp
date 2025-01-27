import os
from utils.logging import Logger
Logger = Logger()
class Config:
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///schoolapp.db"  # Default to SQLite, can be changed to other DB URIs
        self.SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.debug = True
        self.logging_level = "INFO"  # Can be set to DEBUG, INFO, WARNING, ERROR, CRITICAL
        self.user_roles = {
            "student": {"can_post": "approval", "admin_panel_access": False},
            "teacher": {"can_post": "direct", "admin_panel_access": False},
            "admin": {"can_post": "direct", "admin_panel_access": True}
        }
        