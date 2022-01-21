import motor.motor_asyncio
from model import Todo
from dotenv import load_dotenv
import os
import certifi
from model import Todo


load_dotenv()  # take environment variables from .env.
DB_URI = os.environ.get("DB_URI")

# MongoDB Driver

client = motor.motor_asyncio.AsyncIOMotorClient(
    DB_URI, tlsCAFile=certifi.where())
database = client.fastAPI_todo
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todo():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True
