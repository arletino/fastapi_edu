from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id_user == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hash_pwd = user.pwd + 'someHash'
    db_user = models.User(firstname=user.firstname, secondname=user.secondname, email=user.email, pwd=fake_hash_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.UserIn, id_user: int):
    print(user)
    
    test = db.query(models.User).filter(models.User.id_user == id_user)
    test.update(user.model_dump())
    db.commit()
    return get_user(db, id_user)

def delete_user(db: Session, id_user: int):
    user = get_user(db, id_user) 
    db.delete(user) 
    db.commit()
    return user