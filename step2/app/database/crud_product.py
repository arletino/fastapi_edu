from sqlalchemy.orm import Session

from . import models, schemas

def get_product(db: Session, id_product: int):
    return db.query(models.Product).filter(models.Product.id_product == id_product).first()

def get_product_by_product_name(db: Session, product_name: str):
    return db.query(models.Product).filter(models.Product.product_name == product_name).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductIn):
    db_product = models.Product(
        product_name=product.product_name, 
        description=product.description, 
        price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product: schemas.ProductIn, id_product: int):
    test = db.query(models.Product).filter(models.Product.id_product == id_product)
    test.update(product.model_dump())
    db.commit()
    return get_product(db, id_product)

def delete_product(db: Session, id_product: int):
    product = get_product(db, id_product) 
    db.delete(product) 
    db.commit()
    return product