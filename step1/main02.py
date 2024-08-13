from fastapi import FastAPI, Request
import uvicorn
import logging
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
class Task(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[bool] = True

lst_task = []
for i in range(5):
    task = Task(name=f'name_{i}', description=f'desc test {i}', status=True)
    lst_task.append(task)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get('/tasks')
async def get_tasks():
    logger.info('Get list of tasks')
    return lst_task 

@app.get('/tasks/{id}')
async def get_task(id:int):
    try:
        task = lst_task[id]
    except IndexError as e:
        logger.exception(e)
        return JSONResponse(content={"message": "Task not exist"}, status_code=404)
    else:
        logger.info('Get task by id')
    return task

@app.post('/tasks')
async def add_task(task:Task):
    lst_task.append(task)
    logger.info(f'Task {task} add to task list')
    return task

@app.put('/task/{id}')
async def change_task(id:int, task:Task):
    try:
        lst_task[id] = task
    except IndexError as e:
        logger.exception(e)
        return JSONResponse(content={"message": "Task not exist"}, status_code=404)
    else:
        logger.info(f'Change task {id} done')
    return task
    
@app.delete('/task/{id}')
async def del_task(id:int):
    '''Task will not be delete complete, just change status in False'''
    try:
        lst_task[id].status = False
    except IndexError as e:
        return JSONResponse(content={"message": "Task not exist"}, status_code=404)
    return lst_task

if __name__ == '__main__':
    uvicorn.run('main02:app', host="0.0.0.0", port=8080, reload=True)