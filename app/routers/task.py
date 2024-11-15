from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def all_tasks():
    pass

@router.get('/task_id')
async def task_by_id(task_id):
    pass

@router.post('/create')
async def create_task(title, content, priority):
    pass

@router.put('/update')
async def update_task(task_id, title, content, priority):
    pass

@router.delete('/delete')
async def delete_task(task_id):
    pass

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))