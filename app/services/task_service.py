from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database.models import Task
from app.schemas.task import TaskCreate


class TaskService:

    @staticmethod
    def create_task(task_data: TaskCreate, db: Session) -> Task:
        new_task = Task(
            title=task_data.title,
            description=task_data.description
        )

        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        return new_task

    @staticmethod
    def list_tasks(db: Session):
        return db.query(Task).all()

    @staticmethod
    def get_task(task_id: int, db: Session) -> Task:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    @staticmethod
    def delete_task(task_id: int, db: Session):
        task = TaskService.get_task(task_id, db)
        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}
