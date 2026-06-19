from schemas.task import TaskCreate, TaskResponse
from fastapi import APIRouter, HTTPException, status, Depends
from database import get_db
from models.task import Task
from sqlalchemy.orm import Session

router = APIRouter()

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

def get_current_user():
    return {
        'id':1,
        'name':'adit'
    }

@router.get('/profile')
def profile(user = Depends(get_current_user)):
    
    return user

@router.get('/tasks')
def get_tasks(db : Session = Depends(get_db)):
    return db.query(Task).all()
    
@router.get('/tasks/{task_id}')
def get_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
        
    raise HTTPException(status_code=404, detail="Tasks doesnt exist")

@router.post('/tasks')
def create_task(task : TaskCreate, db : Session = Depends(get_db)):
    new_task = Task(
        task = task.task
    )
    db.add(new_task)
    db.commit()
    return {
        'message' : 'Berhasil di tambahkan'
    }

@router.put('/tasks/{task_id}')
def replace_task(task_id:int, task:TaskCreate):
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["task"] = task.task
            
            return existing_task
    
    return {'message' : 'ID Tidak di temukan'}

@router.delete('/tasks/{task_id}')
def delete_task(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {'Message' : f'Task {task_id} berhasil di hapus'} 
    return {'Message' : 'Task tidak di temukan'}