import os

import motor.motor_asyncio
from beanie import init_beanie
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.main import get_application, start_db
from app.core.config import Settings
from app.models.summaries import Summary
from app.db.database import init_db


def get_settings_override():
    return Settings(TESTING=1, DATABASE_URL=os.environ.get("DATABASE_TEST_URL"))


async def override_init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("DATABASE_URL"))
    db = client.summaries_test

    await init_beanie(database=db, document_models=[Summary])


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope="module")
def test_app():
    app = get_application()
    # app.dependency_overrides[Settings] = get_settings_override()
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
async def test_app_with_db():
    app = get_application()
    app.dependency_overrides[Settings] = get_settings_override()
    app.dependency_overrides[start_db] = await override_init_db()
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
