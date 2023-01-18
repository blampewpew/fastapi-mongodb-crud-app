import os

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.config import Settings


def get_settings_override():
    return Settings(TESTING=1, DATABASE_URL=os.environ.get("TEST_DATABASE_URL"))


@pytest.fixture(scope="module")
def test_app():
    app.dependency_overrides[Settings] = get_settings_override()
    with TestClient(app) as test_client:
        yield test_client


