from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from database import crud_orders, models, schemas
from database.database import SessionLocal, engine

import uvicorn

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/orders', tags=['Create orders'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/o")
def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_orders.get_orders(db, skip=skip, limit=limit)
    return users

@router.get("/{id_order}")
def get_order(id_order: int, db: Session = Depends(get_db)):
    order = crud_orders.get_order(db, id_order)
    if not order:
        raise HTTPException(status_code=400, detail=f"Order with {id_order} not found")
    return order


@router.post("/", response_model=schemas.OrderCreate)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = crud_orders.get_order_by_user_id_product_id(db, user_id=order.user_id, product_id=order.product_id)
    if db_order:
        raise HTTPException(status_code=400, 
                            detail=f"Order with such user_id{order.user_id} and product_id{order.product_id} already exist")
    return crud_orders.create_order(db=db, order=order)

@router.put('/{id_order}', response_model=schemas.OrderCreate)
def update_order(id_order: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = crud_orders.get_order(db, id_order)
    if not db_order:
        raise HTTPException(status_code=400, detail="Order not exist")
    return crud_orders.update_order(db, order, id_order)

@router.delete('/{id_order}')
def delete_order(id_order: int, db: Session = Depends(get_db)):
    db_order = crud_orders.get_order(db, id_order)
    if not db_order:
        raise HTTPException(status_code=400, detail="Order not exist")
    return crud_orders.delete_order(db, id_order)


@router.get("/fake_orders/{num}")
def create_fake_orders(num:int, db: Session = Depends(get_db)):
    orders = []
    for i in range(num):
        order  = schemas.OrderCreate(user_id=i, product_id=i) 
        order.append(order)
        crud_orders.create_order(db, order)
    return orders