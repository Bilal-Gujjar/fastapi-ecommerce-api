#app/schemas/user.py
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    userId: UUID
    is_active: bool = True
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
     email: Optional[str] = None

class LoginForm(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str