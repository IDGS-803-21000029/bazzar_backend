# models/product.py
from sqlalchemy import Column, Integer, String, Float
from db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    discountPercentage = Column(Float)
    rating = Column(Float)
    stock = Column(Integer)
    brand = Column(String)
    category = Column(String)
    thumbnail = Column(String)
    images = Column(String)
