from sqlalchemy import Column, Integer, String, Float
from ..core.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)  # No need to explicitly define Sequence
    name = Column(String(100))
    description = Column(String(300))
    price = Column(Float)
    in_stock = Column(Integer)
