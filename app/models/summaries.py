from datetime import datetime

from beanie import Document
from typing import Optional


class Summary(Document):
    url: str
    summary: Optional[str]
    created_at: datetime = datetime.now()

    class Settings:
        name = "summaries"

    class Config:
        schema_extra = {
            "example": {
                "url": "example.com",
                "summary": "summary goes here.",
                "created_at": datetime.now()
            }
        }