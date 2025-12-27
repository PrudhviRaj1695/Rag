from backend.app.evaluation.evaluator import run_evaluation

if __name__ == "__main__":
    results = run_evaluation()
    for r in results:
        print(r)
