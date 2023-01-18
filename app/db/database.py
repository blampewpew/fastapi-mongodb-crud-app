from beanie import init_beanie
import motor.motor_asyncio

from app.models.summaries import Summary


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        # Will need to make this pull from the ENV variable
        "mongodb://localhost:27017/summaries"
    )

    await init_beanie(database=client.db_name, document_models=[Summary])
