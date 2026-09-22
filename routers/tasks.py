from fastapi import APIRouter, Depends, status, HTTPException
from schemas.task import TaskCreate, TaskUpdate, TaskOut
from sqlalchemy.orm import Session
from database import get_db
from models.task import Task
from sqlalchemy import select, delete
router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    try:
        tasks = db.scalars(select(Task).order_by(Task.id)).all()
        return tasks
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal serveer error")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session=Depends(get_db)):
    if not task.description:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="The description field can not be empty")
    task = Task(
            title=task.title,
            description=task.description,
            due_date=task.due_date
        )
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"success": True, "message":"Task created successfully"}

@router.put("/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    pass

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"success": True, "message": "task deleted successfully"}

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TaskOut)
def get_single_task(id: int, db: Session = Depends(get_db)):
        get_task = db.scalars(
            select(Task).where(Task.id == id)
        ).first()

        if get_task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

        return get_task