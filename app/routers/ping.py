from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.models.summaries import Summary

router = APIRouter()


@router.get("/ping")
async def pong() -> dict:
    return {"ping": "pong!"}