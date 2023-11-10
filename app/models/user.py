# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)  # Auto-incremented by PostgreSQL
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    hashed_password = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Add relationships and any additional columns here
