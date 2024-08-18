from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from database import crud_user, models, schemas
from database.database import SessionLocal, engine

import uvicorn

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/users', tags=['Create users'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}")
def read_users(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(db, user_id)
    print(user)
    if not user:
        raise HTTPException(status_code=400, detail=f"User with {user_id} not found")
    return user


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exist")
    return crud_user.create_user(db=db, user=user)

@router.put('/{id_user}', response_model=schemas.UserIn)
def update_user(id_user: int, user: schemas.UserIn, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, id_user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not exist")
    return crud_user.update_user(db, user, id_user)

@router.delete('/{id_user}')
def delete_user(id_user: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, id_user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not exist")
    return crud_user.delete_user(db, id_user)


# @router.get("/fake_users/{num}")
# def create_fake_user(num:int, db: Session = Depends(get_db)):
#     users = []
#     for i in range(num):
#         user  = schemas.UserCreate(firstname=f'name{i}', secondname=f'secname{i}', email=f'email{i}@mail.com', pwd=f'pwd_user{i}') 
#         users.append(user)
#         crud_user.create_user(db, user)
#     return users



if __name__ == '__main__':
    uvicorn.run('main:router', host="0.0.0.0", port=8080, reload=True)