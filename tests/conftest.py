import os

import pytest
from starlette.testclient import TestClient

from app.main import get_application
from app.core.config import settings


def get_settings_override():
    return settings(TESTING=1, DATABASE_URL=os.environ.get("TEST_DATABASE_URL"))


@pytest.fixture(scope="module")
def test_app():
    app = get_application()
    app.dependency_overrides[settings] = get_settings_override()
    with TestClient(app) as test_client:
        yield test_client


