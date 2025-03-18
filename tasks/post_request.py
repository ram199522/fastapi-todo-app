from fastapi import APIRouter
from config import collection


router = APIRouter()

@router.post("/tasks/")
async def create_task(task:dict):
	result = await collection.insert_one(task) #after inserting it will return a mongodb unique_id("_id")
	return{"message":"Task created successfully","id":str(result.inserted_id)}