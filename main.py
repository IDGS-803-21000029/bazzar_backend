# main.py
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db import engine, Base, SessionLocal
from models.product import Product
from models.sale import Sale
from models.schemas import ProductSchema, SaleSchema
from typing import List
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",  # Habilita localhost (útil para pruebas locales)
    "http://177.228.62.53:5173",  # Habilita localhost en un puerto específico (ej., React/Angular en el puerto 3000)
    #"https://tu-dominio.com",  # Habilita tu dominio de producción
    # Puedes agregar más dominios según tus necesidades
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite los orígenes definidos en la lista
    allow_credentials=True,  # Permite el envío de cookies
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Carga los datos de seed al iniciar la aplicación
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        load_seed_data(db)
    finally:
        db.close()

def load_seed_data(db: Session):
    # Verifica si ya hay productos en la base de datos
    if db.query(Product).count() > 0:
        print("La base de datos ya contiene productos.")
        return

    # Lee el archivo JSON
    with open("products.json", "r") as file:
        data = json.load(file)
        products_data = data["products"]  # Accede a la lista de productos
    
    # Itera sobre los datos del JSON e inserta cada producto
    for product_data in products_data:
        # Convierte la lista de imágenes en una cadena separada por comas
        images_str = ",".join(product_data["images"])
        
        product = Product(
            id=product_data["id"],
            title=product_data["title"],
            description=product_data["description"],
            price=product_data["price"],
            discountPercentage=product_data["discountPercentage"],
            rating=product_data["rating"],
            stock=product_data["stock"],
            brand=product_data["brand"],
            category=product_data["category"],
            thumbnail=product_data["thumbnail"],
            images=images_str
        )
        db.add(product)
    db.commit()
    print("Datos de seed agregados a la base de datos.")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/items", response_model=List[ProductSchema])
def search_items(q: str = Query(None), db: Session = Depends(get_db)):
    items = db.query(Product).filter(Product.title.ilike(f"%{q}%")).all()
    return items

@app.get("/api/items/{id}", response_model=ProductSchema)
def get_item(id: int, db: Session = Depends(get_db)):
    item = db.query(Product).filter(Product.id == id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

class SaleRequest(BaseModel):
    product_id: int

@app.post("/api/addSale")
def add_sale(request: SaleRequest, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == request.product_id).first()
    if not product:
        return {"success": False}
    
    sale = Sale(product_id=request.product_id)
    db.add(sale)
    db.commit()
    return {"success": True}

@app.get("/api/sales/", response_model=List[SaleSchema])
def get_sales(db: Session = Depends(get_db)):
    sales = db.query(Sale).join(Product).all()
    return sales

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

