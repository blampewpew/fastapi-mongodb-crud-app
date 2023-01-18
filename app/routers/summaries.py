from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.models.summaries import Summary

router = APIRouter()


@router.post("/", response_description="Summary added to the database")
async def add_summary(summary: Summary) -> dict:
    summary = await summary.create()
    return summary