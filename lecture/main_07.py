import databases
import sqlalchemy
from fastapi import FastAPI

DATABASES_URL = 'sqlite: ///my_database.db'
databases = databases.Database(DATABASES_URL)
metadata = sqlalchemy.MetaData()


...

engine = sqlalchemy.create_engine(DATABASES_URL)