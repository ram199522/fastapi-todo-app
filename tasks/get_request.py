from fastapi import APIRouter, HTTPException
from bson import ObjectId
from config import collection

router = APIRouter()

@router.get("/tasks/")
async def get_all_tasks():
	tasks = await collection.find().to_list(30)
	for task in tasks:
		task["id"] = str(task["_id"])
		del task["_id"]
	return tasks

@router.get("/tasks/{task_id}")
async def get_task_by_id(task_id:str):
	task = await collection.find_one({"_id":ObjectId(task_id)})
	if not task:
		raise HTTPException(status_code=404,detail="Task not found")
	task["id"] = str(task["_id"])
	del task["_id"]
	return task
