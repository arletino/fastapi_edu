from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()


@app.get('/items/{item_id}')
async def read_item(item_id: int = Path(..., title='The ID of the item', ge=1), q: str = None):
    return {'item_id': item_id, 'q': q}

if __name__ == '__main__':
    uvicorn.run('main_path:app', host='0.0.0.0', port=8080, reload=True )