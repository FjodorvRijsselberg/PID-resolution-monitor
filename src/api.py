import requests
from fastapi import APIRouter
from version import get_version

router = APIRouter()


@router.get("/version")
async def info():
    result = get_version()
    return {"version": result}
