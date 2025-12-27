from fastapi import FastAPI
from backend.app.routes.chat import router as chat_router

from util.logger import logger

app = FastAPI(title="RAG Backend")

logger.info("Starting RAG request")

app.include_router(chat_router, prefix="/chat")

@app.get("/health")
def health():
    return {"status": "ok"}
