from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.task import TaskCreate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return TaskService.create_task(task, db)


@router.get("/")
def list_tasks(db: Session = Depends(get_db)):
    return TaskService.list_tasks(db)


@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    return TaskService.get_task(task_id, db)


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return TaskService.delete_task(task_id, db)
