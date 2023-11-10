from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SaleBase(BaseModel):
    product_id: int
    amount: float

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True
