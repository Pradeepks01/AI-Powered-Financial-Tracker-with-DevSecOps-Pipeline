import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI-Powered Financial Tracker"
    
    # Database config
    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "Test%40123")
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE", "financial_db")
    
    # Construct DATABASE_URL if not explicitly provided
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )
    
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key-for-dev-only")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
