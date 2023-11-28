# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID  # Import this for UUID
import uuid  # This is for generating UUID values
from datetime import datetime
from app.core.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    userId= Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    hashed_password = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)