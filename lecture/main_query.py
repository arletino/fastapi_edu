from fastapi import FastAPI, Query
import uvicorn


app = FastAPI()

@app.get('/items/')
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    results = {'items_id': 'Spam'}, {'item_id': 'Eggs'}
    if q:
        results.updates({'q': q})
    return results

if __name__ == '__main__':
    uvicorn.run('main_query:app', host='0.0.0.0', port=8080, reload=True )