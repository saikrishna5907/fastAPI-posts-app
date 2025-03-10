from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

encoded_password = quote(settings.POSTGRES_PASSWORD) # URL encode the password to handle special characters in the password ex: @, #, $, etc.

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.POSTGRES_USER}:{encoded_password}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()