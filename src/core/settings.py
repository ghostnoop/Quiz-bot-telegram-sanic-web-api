import os

from sanic_envconfig import EnvConfig
from dotenv import load_dotenv, find_dotenv, dotenv_values


class Settings(EnvConfig):
    config = dotenv_values(find_dotenv())
    DEBUG: bool = config.get('DEBUG', False)
    HOST: str = config.get('HOST', 'localhost')
    PORT: int = config.get('PORT', 8000)
    DB_URL: str = config.get('DB_URL', 'postgresql://postgres:postgres@localhost/quizdb')

    TOKEN: str = config.get('TOKEN', None)
    CHANNEL = config.get("CHANNEL", '@testquiz')
