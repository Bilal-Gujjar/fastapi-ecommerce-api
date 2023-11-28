from pydantic import BaseModel

class InventoryBase(BaseModel):
    product_id: int
    quantity_no: int
    in_stock: int  

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int

    class Config:
        orm_mode = True
