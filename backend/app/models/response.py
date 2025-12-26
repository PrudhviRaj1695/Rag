from pydantic import BaseModel
from typing import List

class Source(BaseModel):
    document: str
    page: int

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
