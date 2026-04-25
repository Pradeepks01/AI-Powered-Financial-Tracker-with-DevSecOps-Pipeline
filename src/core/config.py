import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI-Powered Financial Tracker"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://root:Test%40123@localhost:3306/financial_db")
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key-for-dev-only")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
