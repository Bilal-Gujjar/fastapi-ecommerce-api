# /app/api/endpoints/product.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ....models.product import Product as DBProduct
from ....schemas.product import ProductCreate, Product as ProductSchema
from app.core.database import get_db

router = APIRouter()

@router.post("/products/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = DBProduct(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

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

# Implement PUT and DELETE operations as needed
