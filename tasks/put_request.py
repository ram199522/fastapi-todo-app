from fastapi import APIRouter,HTTPException
from config import collection
from bson import ObjectId


router = APIRouter()


@router.put("/tasks/{task_id}")
async def update_task(task_id:str,task_to_update:dict):
	result = await collection.update_one({"_id":ObjectId(task_id)},{"$set":task_to_update})
	if result.matched_count == 0:
		raise HTTPException(status_code=404,detail="Task not found")
	return {"message":"Task updated successfully"}