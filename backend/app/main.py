from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="RAG Backend")

app.include_router(chat_router, prefix="/chat")

@app.get("/health")
def health():
    return {"status": "ok"}
