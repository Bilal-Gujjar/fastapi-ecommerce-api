# /app/api/endpoints/inventory.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....models.inventory import Inventory as DBInventory
from app.core.database  import get_db

router = APIRouter()

@router.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):
    return db.query(DBInventory).all()
