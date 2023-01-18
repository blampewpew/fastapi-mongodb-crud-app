import json

import pytest


@pytest.mark.anyio
async def test_create_summary(test_app_with_db):
    response = await test_app_with_db.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))

    assert response.status_code == 200
    assert response.json()["url"] == "https://foo.bar"
