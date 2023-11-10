from sqlalchemy import Column, Integer, Sequence, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..core.database import Base

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, Sequence('sale_id_seq'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)
    product = relationship("Product")
