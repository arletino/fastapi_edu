from fastapi import FastAPI
from database import models
import routers.user as user
import routers.product as product
import routers.order as order
from database.database import SessionLocal, engine

import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router, tags=['users'])
app.include_router(product.router, tags=['products'])
app.include_router(order.router, tags=['orders'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True)