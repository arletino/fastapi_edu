from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from database import crud_product, models, schemas
from database.database import SessionLocal, engine

import uvicorn

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/products', tags=['Create product'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_product.get_products(db, skip=skip, limit=limit)
    return users

@router.get("/{id_product}")
def get_product(id_product: int, db: Session = Depends(get_db)):
    product = crud_product.get_product(db, id_product)
    print(product)
    if not product:
        raise HTTPException(status_code=400, detail=f"Product with {id_product} not found")
    return product


@router.post("/", response_model=schemas.ProductIn)
def create_product(product: schemas.ProductIn, db: Session = Depends(get_db)):
    db_product = crud_product.get_product_by_product_name(db, product_name=product.product_name)
    if db_product:
        raise HTTPException(status_code=400, detail=f"Product with such name{product.product_name} already exist")
    return crud_product.create_product(db=db, product=product)

@router.put('/{id_product}', response_model=schemas.ProductIn)
def update_product(id_product: int, product: schemas.ProductIn, db: Session = Depends(get_db)):
    db_product = crud_product.get_product(db, id_product)
    if not db_product:
        raise HTTPException(status_code=400, detail="Product not exist")
    return crud_product.update_product(db, product, id_product)

@router.delete('/{id_product}')
def delete_product(id_product: int, db: Session = Depends(get_db)):
    db_product = crud_product.get_product(db, id_product)
    if not db_product:
        raise HTTPException(status_code=400, detail="Product not exist")
    return crud_product.delete_product(db, id_product)


@router.get("/fake_products/{num}")
def create_fake_products(num:int, db: Session = Depends(get_db)):
    products = []
    for i in range(num):
        product  = schemas.ProductIn(product_name=f'name{i}', description=f'description{i}', price= (1.0+i)) 
        product.append(product)
        crud_product.create_product(db, product)
    return products



if __name__ == '__main__':
    uvicorn.run('main:router', host="0.0.0.0", port=8080, reload=True)