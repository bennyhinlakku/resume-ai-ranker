RETRIEVAL_KEYWORDS = {

    "retrieval": 3,
    "ranking": 3,
    "recommendation": 3,
    "search": 2,
    "matching": 2,
    "embeddings": 2,
    "embedding": 2,
    "vector": 2,
    "semantic": 2,
    "similarity": 2,
    "bm25": 3,
    "faiss": 3,
    "milvus": 3,
    "pinecone": 3,
    "weaviate": 3,
    "qdrant": 3,
    "elasticsearch": 2,
    "opensearch": 2
}


def retrieval_score(career_text):

    career = career_text.lower()

    score = 0
    matched = []

    for keyword, weight in RETRIEVAL_KEYWORDS.items():

        if keyword in career:
            score += weight
            matched.append(keyword)

    return {

        "retrieval_score": score,
        "matched_keywords": matched
    }


if __name__ == "__main__":

    sample = """
    Designed semantic search using embeddings.
    Built a recommendation engine.
    Used Milvus for vector retrieval.
    Improved ranking quality.
    """

    result = retrieval_score(sample)

    print("=" * 60)

    for k, v in result.items():
        print(f"{k}: {v}")

    print("=" * 60)