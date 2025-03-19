import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("MONGO_URL")
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("COLLECTION_NAME")


# Get API_URL from .env
API_URL = os.getenv("API_URL")

# Raise error if API_URL is missing
if not API_URL:
    raise ValueError("API_URL is missing! Set it in the .env file.")


client = AsyncIOMotorClient(mongo_url)
db = client[db_name]
collection = db[collection_name]