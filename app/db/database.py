import os

from beanie import init_beanie
import motor.motor_asyncio

from app.models.summaries import Summary


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("DATABASE_URL"))
    db = client.summaries

    await init_beanie(database=db, document_models=[Summary])
