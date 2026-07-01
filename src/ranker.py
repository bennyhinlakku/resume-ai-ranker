from feature_engineering import load_candidates, extract_features, DATA_FILE
from scorer import HybridScorer

print("Loading candidates...")
candidates = load_candidates(DATA_FILE)

print(f"Loaded {len(candidates)} candidates")

scorer = HybridScorer()

results = []

for i, candidate in enumerate(candidates):

    features = extract_features(candidate)

    score = scorer.score(features)

    results.append({
        "candidate_id": features["candidate_id"],
        "score": score["total"],
        "breakdown": score
    })

    if (i + 1) % 1000 == 0:
        print(f"Processed {i+1} candidates")

print("Sorting...")

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTop 10 Candidates\n")

for r in results[:10]:
    print(r["candidate_id"], r["score"])