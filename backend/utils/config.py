"""
Configuration management using Pydantic Settings
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings"""
    
    # Database
    DATABASE_URL: str = "sqlite:///./data/database/news.db"
    
    # API Keys
    NEWS_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    
    # Scraping
    SCRAPE_INTERVAL: int = 3600
    MAX_ARTICLES_PER_SOURCE: int = 100
    USER_AGENT: str = "NewsAnalyticsPlatform/1.0"
    
    # Server
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DASHBOARD_PORT: int = 3000
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    
    # Environment
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
