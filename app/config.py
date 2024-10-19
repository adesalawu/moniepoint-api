# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    client_id: str
    client_secret: str
    base_url: str

    class Config:
        env_file = ".env"

settings = Settings()
