import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    def __init__(self):
        self._load_environment_variables()

    def _load_environment_variables(self):
        self.ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
        self.MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8000")
        

SETTINGS = Settings()