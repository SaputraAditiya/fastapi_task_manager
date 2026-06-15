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
    new_task = {
        "id" : len(tasks) + 1,
        "task" : task.task
    }
    tasks.append(new_task)
    return new_task

@app.put('/tasks/{task_id}')
def replace_task(task_id:int, task:CreateTask):
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["task"] = task.task
            
            return existing_task
    
    return {'message' : 'ID Tidak di temukan'}