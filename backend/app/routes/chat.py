from fastapi import APIRouter
from backend.app.services.rag_service import run_rag
from backend.app.models.request import ChatRequest

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    return await run_rag(request.query)
