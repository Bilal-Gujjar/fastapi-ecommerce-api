# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
