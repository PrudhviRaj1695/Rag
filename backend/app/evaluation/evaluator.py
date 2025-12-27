from backend.app.services.retriever import retrieve_chunks
from backend.app.evaluation.dataset import EVAL_DATASET
from backend.app.evaluation.metrics import recall_at_k, precision_at_k

def run_evaluation():
    results = []

    for item in EVAL_DATASET:
        query = item["query"]
        expected = item["expected_doc"]

        retrieved = retrieve_chunks(query, top_k=5)

        recall = recall_at_k(retrieved, expected)
        precision = precision_at_k(retrieved, expected)

        results.append({
            "query": query,
            "recall@5": recall,
            "precision@5": precision
        })

    return results
