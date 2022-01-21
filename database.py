from model import Todo
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
DB_URI = os.environ.get("DB_URI")

# MongoDB Driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
database = client.fastAPI_todo
collection = database.todo