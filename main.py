from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CreateTask(BaseModel):
    task:str

tasks = [
    {
        'id' : 1,
        'task' : 'Belajar Fastapi'
    },
    {
        'id' : 2,
        'task' : 'Kerjakan reimburse app'
    }
]

@app.get('/')
def root() :
    return {'message' : 'Hello Adit'}

@app.get('/tasks')
def get_task() :
    return tasks
    
@app.get('/tasks/{task_id}')
def get_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
        
    return {'message' : 'Task tidak di temukan'}

@app.post('/tasks')
def create_task(task:CreateTask):
    return {
        'message' : 'Berhasil menambahkan',
        'data' : task
    }