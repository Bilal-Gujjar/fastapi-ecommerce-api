# app/api/v1/main.py
from fastapi import APIRouter

from app.api.v1.endpoints import user, sales, product ,auth ,inventory

router = APIRouter()

router.include_router(user.router, prefix="/v1", tags=["users"])
router.include_router(sales.router, prefix="/v1", tags=["sales"])
router.include_router(product.router, prefix="/v1", tags=["products"])
router.include_router(auth.router, prefix="/v1", tags=["auth"])
router.include_router(inventory.router, prefix="/v1", tags=["inventory"])
