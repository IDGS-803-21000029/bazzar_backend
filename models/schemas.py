# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    discountPercentage: Optional[float] = None
    rating: Optional[float] = None
    stock: Optional[int] = None
    brand: Optional[str] = None
    category: Optional[str] = None
    thumbnail: Optional[str] = None
    images: Optional[str] = None

    class Config:
        orm_mode = True

class SaleSchema(BaseModel):
    id: int
    product_id: int
    sale_date: datetime  # Usa el tipo `datetime` si prefieres manejar fechas como objetos de tiempo
    product: ProductSchema

    class Config:
        orm_mode = True
