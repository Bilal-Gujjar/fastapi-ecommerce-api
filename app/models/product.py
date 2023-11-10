from sqlalchemy import Column, Integer, String, Sequence, Float
from ..core.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    name = Column(String(100))
    description = Column(String(300))
    price = Column(Float)
    in_stock = Column(Integer)
