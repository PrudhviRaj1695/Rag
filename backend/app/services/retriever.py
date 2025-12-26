from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from app.config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_INDEX,
    AZURE_SEARCH_KEY,
)

# Initialize search client
search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY),
)

def retrieve_chunks(query: str, top_k: int = 5):
    """
    Retrieves top relevant chunks from Azure Search
    including page number and source.
    """

    results = search_client.search(
        search_text=query,
        top=top_k,
        query_type="semantic",
        semantic_configuration_name="default",
        select=["content", "page", "source"]
    )

    documents = []
    for result in results:
        documents.append({
            "content": result.get("content"),
            "page": result.get("page"),
            "source": result.get("source")
        })

    return documents
