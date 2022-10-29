import beanie
import motor
import motor.motor_asyncio

from data_access.models import User, Blog, Like


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

    await beanie.init_beanie(
        database=client.db_name,
        document_models=[User, Blog, Like]
    )
