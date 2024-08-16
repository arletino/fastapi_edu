import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title='Name', max_length=50)
    price: float = Field(..., title='Price', gt=0, le=10000)
    description: str = Field(default=None, title='Description', max_length=10000)
    tax: float = Field(0, title='Tax', ge=0, le=10)



class User(BaseModel):
    username: str = Field(title="Username", max_length=50)
    full_name: str = Field(None, title='Full Name', max_length=100)



@app.post('/item/')
async def create_item(item: Item):
    return {'item': item}


if __name__ == '__main__':
    uvicorn.run('main06:app', host="0.0.0.0", port=8080, reload=True)