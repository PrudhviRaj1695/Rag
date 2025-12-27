from backend.app.services.retriever import retrieve_chunks
from backend.app.services.llm import ask_llm

async def run_rag(query: str):
    documents = retrieve_chunks(query)

    context = "\n\n".join(
        f"Source: {d['source']} | Page: {d['page']}\n{d['content']}"
        for d in documents
    )

    prompt = f"""
You are a helpful assistant.
Use only the context below to answer.

{context}

Question: {query}
"""

    answer = ask_llm(prompt)
    return {"answer": answer, "sources": documents}
