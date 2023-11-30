# /app/api/endpoints/product.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from typing import List
from ....models.product import Product as DBProduct
from ....models.inventory import Inventory as DBInventory
from ....schemas.product import ProductCreate, Product as ProductSchema
from app.core.database import get_db
import logging

router = APIRouter()

@router.post("/products/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        db_product = DBProduct(name=product.name, description=product.description, price=product.price)
        db.add(db_product)
        db.flush()

        inventory_entry = DBInventory(product_id=db_product.id, quantity_no=product.initial_stock, in_stock=product.initial_stock)
        db.add(inventory_entry)

        db.commit()
        return db_product

    except SQLAlchemyError as e:
        db.rollback()
        logging.error(f"SQLAlchemyError occurred: {e}")
        raise HTTPException(status_code=500, detail="Failed to create product due to a database error.")



@router.get("/products/", response_model=List[ProductSchema])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(DBProduct).offset(skip).limit(limit).all()
    return products

@router.get("/products/{product_id}", response_model=ProductSchema)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
