"""Load configuration settings from the .env file"""
import os
from dotenv import load_dotenv

class Config:
    """
    Config is a singleton class responsible for managing the application's settings.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def __init__(self):
        self._load_config()

    def _load_config(self):
        load_dotenv(override=True)
        self.environment = os.getenv("ENVIRONMENT")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")

config = Config()
