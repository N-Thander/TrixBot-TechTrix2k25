
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return{
        "message" : "Welcome to Trix-Bot API",
        "version" : "1.0.0",
        "description" : "AI Chat Bot for TechTrix 2025"
    }