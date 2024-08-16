import databases
import sqlalchemy
from fastapi import FastAPI
from contextlib import asynccontextmanager

DATABASE_URL = 'sqlite:///sqlitebd.db'

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

...

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)



@asynccontextmanager
async def lifespan(app: FastAPI):
    database.connect()
    yield
    database.disconnect()

app = FastAPI(lifespan=lifespan)

# @app.on_event('startup')
# async def startup():
#     await database.connect



# @app.on_event('shutdown')
# async def shutdown():
#     await database.disconnect
