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
def get_tasks(
    db : Session = Depends(get_db) 
):
    
    return db.query(Task).all()
    
@router.get('/tasks/{task_id}')
def get_task(
    task_id : int, 
    db : Session = Depends(get_db)
):
    
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()
    
    if not task:
        raise HTTPException(
            status_code=404, 
            detail="Tasks doesnt exist"
        )
    
    return task

@router.post('/tasks')
def create_task(
    task : TaskCreate, 
    db : Session = Depends(get_db)
):
    
    new_task = Task(
        task = task.task
    )
    
    db.add(new_task)
    
    db.commit()
    
    return {
        'message' : 'Berhasil di tambahkan'
    }

@router.put('/tasks/{task_id}')
def replace_task(task_id : int, 
                 new_task : TaskCreate, 
                 db : Session = Depends(get_db)
):
    
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()
    
    if not task:
        raise HTTPException(
            status_code=404, 
            detail="Tasks doesnt exist"
        )
    
    task.task = new_task.task
    
    db.commit()
    
    db.refresh(task)
    
    return task

@router.delete('/tasks/{task_id}')
def delete_task(task_id:int,
                db : Session = Depends(get_db)
):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tasks doesnt exist"
        )
    
    db.delete(task)
    
    db.commit()
        
    return {'Message' : f'Task {task_id} berhasil di hapus'}