from sqlalchemy import Column, Integer, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Inventory(Base):
    __tablename__ = 'inventories'
    id = Column(Integer, Sequence('inventory_id_seq'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity_no = Column(Integer)
    product = relationship("Product")
