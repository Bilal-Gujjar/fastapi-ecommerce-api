from sqlalchemy.orm import Session
from ..models import Inventory
from ..schemas import InventoryCreate

def get_inventory(db: Session, product_id: int):
    return db.query(Inventory).filter(Inventory.product_id == product_id).first()

def create_inventory(db: Session, inventory: InventoryCreate):
    db_inventory = Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory
