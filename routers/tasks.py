from fastapi import APIRouter
from schemas.task import TaskCreate, TaskUpdate, TaskOut

router = APIRouter(prefix="/task", tags=["Tasks"])

@router.get("/")
def get_tasks():
    pass

@router.post("/")
def create_task():
    pass

@router.put("/{task_id}")
def update_task():
    pass

@router.delete("/{task_id}")
def delete_task():
    pass

@router.get("/{task_id}")
def get_single_task():
    pass