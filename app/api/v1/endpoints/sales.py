# /app/api/endpoints/sales.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ....models.sales import Sale as DBSale
from ....models.product import Product as DBProduct
from app.core.database import get_db


router = APIRouter()

@router.get("/sales")
def get_sales_data(db: Session = Depends(get_db)):
    sales_data = db.query(DBSale).all()
    return sales_data

@router.get("/sales/profit")
def get_profit_data(db: Session = Depends(get_db)):
    profit_data = (
        db.query(
            DBSale.product_id,
            func.sum(DBSale.amount).label("total_sales_amount"),
            func.count(DBSale.id).label("number_of_sales"),
            func.sum(DBSale.amount - DBProduct.price).label("total_profit")
        )
        .join(DBProduct)
        .group_by(DBSale.product_id)
        .all()
    )
    return profit_data
