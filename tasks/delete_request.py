from fastapi import APIRouter, HTTPException
from bson import ObjectId
from config import collection

router = APIRouter()


@router.delete("/tasks/{task_id}")
async def delete_task(task_id:str):
	result = await collection.delete_one({"_id":ObjectId(task_id)})
	if result.deleted_count == 0:
		raise HTTPException(status_code=404,detail="Task not found")
	return {"message":"Task deleted successfully"}