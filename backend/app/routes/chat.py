from fastapi import APIRouter
from app.services.rag_service import run_rag
from app.models.request import ChatRequest

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    return await run_rag(request.query)
