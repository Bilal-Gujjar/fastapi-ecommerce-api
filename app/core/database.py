#app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import text

# Import the settings instance from your config module
from .config import settings

# Retrieve the DATABASE_URL from the settings
# print(settings.database_url)
DATABASE_URL = settings.database_url

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a scoped session
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = scoped_session(session_factory)

# Base class for your models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        # Try to execute a simple "SELECT 1" command to check if the database is connected
        db.execute(text("SELECT 1"))
        print("Database connected.")
        yield db
    except OperationalError as e:
        print("Database connection error:", e)
        raise e
    finally:
        db.close()
