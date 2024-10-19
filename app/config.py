"""
Author's Note:
This script serves as the entry point of the FastAPI application. It initializes the app, sets up routes, and launches the server using Uvicorn. 

The goal is to provide a high-performance API for handling push payment requests and transaction status using Moniepoint's gateway.

Feel free to modify the routes or add additional middleware as needed to extend the functionality.

Author: Adediran
Contact: adesalawu@icloud.com
"""
# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    client_id: str
    client_secret: str
    base_url: str

    class Config:
        env_file = ".env"

settings = Settings()
