import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

from app.config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_INDEX,
    AZURE_SEARCH_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
)

# --------------------------------------------------
# Clients
# --------------------------------------------------

search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY),
)

openai_client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION,
)

# --------------------------------------------------
# Load & chunk document
# --------------------------------------------------

def load_and_split_pdf(file_path: str):
    reader = PdfReader(file_path)
    chunks = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if not text:
            continue

        for chunk in splitter.split_text(text):
            chunks.append({
                "content": chunk,
                "page": page_num
            })

    return chunks


# --------------------------------------------------
# Embed and index
# --------------------------------------------------

def index_document(file_path: str):
    chunks = load_and_split_pdf(file_path)

    documents = []
    for i, chunk in enumerate(chunks):
        embedding = openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk["content"]
        ).data[0].embedding

        documents.append({
            "id": f"doc-{i}",
            "content": chunk["content"],
            "page": chunk["page"],
            "source": os.path.basename(file_path),
            "embedding": embedding
        })

    result = search_client.upload_documents(documents=documents)
    print(f"✅ Indexed {len(documents)} chunks")
    return result


# --------------------------------------------------
# Run directly
# --------------------------------------------------
if __name__ == "__main__":
    index_document(
        r"C:\Users\prudh\OneDrive\Desktop\RAG\RAG_Project\backend\app\services\hdfc-life-sampoorn-nivesh-plus-v01-policy-bond.pdf"
    )
