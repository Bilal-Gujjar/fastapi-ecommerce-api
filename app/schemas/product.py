from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    price: float

class ProductCreate(ProductBase):
    price: float
    initial_stock: Optional[int] = None

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True
        from_attributes = True
