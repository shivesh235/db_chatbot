from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database Configuration
    POSTGRES_USER: str = "db1"
    POSTGRES_PASSWORD: str = "1234"
    POSTGRES_DB: str = "supplier_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"

    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Free LLM Model
    LLM_MODEL: str = "facebook/opt-1.3b"  # A more powerful free model

    # Security
    JWT_SECRET: str = "your-secret-key"

    class Config:
        env_file = ".env"

settings = Settings()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()