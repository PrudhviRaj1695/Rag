from app.services.index_documents import index_documents

docs = [
    {
        "content": "Health insurance claims must be submitted within 30 days of treatment.",
        "source": "policy.pdf"
    },
    {
        "content": "Pre-authorization is required for elective surgeries.",
        "source": "policy.pdf"
    }
]

index_documents(docs)
