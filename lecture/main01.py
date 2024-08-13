from fastapi import FastAPI, Request
import uvicorn
import logging
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates


class Item(BaseModel):
    name: str
    decription: Optional[str] = None
    price: float
    tax: Optional[float] = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory='./templates')

@app.get('/', response_class=HTMLResponse)
async def read_root():
    logger.info('GET request done')
    return '<h1>Hello World<h1>'

@app.get('/{name}', response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    print(request)
    return templates.TemplateResponse('item.html', {'request': request, 'name': name})


@app.get('/message')
async def read_messages():
    message = {'message': 'Hello World'}
    return JSONResponse(content=message, status_code=200)

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    if q: 
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.get('/users/{user_id}/orders/{order_id}')
async def read_data(user_id: int, order_id: int):
    # operation with data
    return {'user_id': user_id, 'order_id': order_id}

@app.get('/items/')
async def skip_limit(skip: int = 0, limit: int = 10):
    answer = []
    for i in range(limit):
        answer.append({'skip': i, 'limit': limit})
    return answer

@app.post('/items/')
async def create_item(item: Item):
    logger.info('POST request done')
    return item

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    logger.info(f'PUT request done for item id = {item_id}')
    return {'item_id': item_id, 'item': item}

@app.delete('/items/{item_id}')
async def update_item(item_id: int):
    logger.info(f'DELETE request done got item id = {item_id}')
    return {'item_id': item_id}


if __name__ == '__main__':
    uvicorn.run('main01:app', host="0.0.0.0", port=8080, reload=True)