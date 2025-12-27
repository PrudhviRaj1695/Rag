def recall_at_k(retrieved_docs, expected_doc_id, k=5):
    top_k = retrieved_docs[:k]
    return int(any(doc["source"] == expected_doc_id for doc in top_k))


def precision_at_k(retrieved_docs, expected_doc_id, k=5):
    top_k = retrieved_docs[:k]
    hits = sum(1 for d in top_k if d["source"] == expected_doc_id)
    return hits / k
