from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Inventory(Base):
    __tablename__ = 'inventories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity_no = Column(Integer) 
    in_stock = Column(Integer) 
    product = relationship("Product")
