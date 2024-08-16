from sqlalchemy.orm import Session

from . import models, schemas

def get_order(db: Session, id_order: int):
    return db.query(models.Order).filter(models.Order.id_order == id_order).first()

def get_order_by_user_id_product_id(db: Session, user_id: str,  product_id: int):
    return db.query(models.Order).filter(models.Order.user_id == user_id, models.Order.product_id == product_id ).first()

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        user_id=order.user_id, 
        product_id=order.product_id
        )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order: schemas.OrderCreate, id_order: int):
    test = db.query(models.Order).filter(models.Order.id_order == id_order)
    test.update(order.model_dump())
    db.commit()
    return get_order(db, id_order)

def delete_order(db: Session, id_order: int):
    order = get_order(db, id_order) 
    db.delete(order) 
    db.commit()
    return order