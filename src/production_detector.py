PRODUCTION_KEYWORDS = [

    "production",
    "deployed",
    "deployment",
    "real-time",
    "real users",
    "millions",
    "pipeline",
    "streaming",
    "serving",
    "inference",
    "feature store",
    "monitoring",
    "evaluation",
    "a/b",
    "recommendation",
    "ranking",
    "retrieval",
    "search",
    "vector",
    "embedding"
]


def production_score(career_text):

    career = career_text.lower()

    matched = []

    score = 0

    for keyword in PRODUCTION_KEYWORDS:

        if keyword in career:
            score += 1
            matched.append(keyword)

    return {

        "production_score": score,

        "matched_keywords": matched
    }


if __name__ == "__main__":

    sample = """
    Built a recommendation system serving
    millions of users using vector retrieval.
    Designed production ranking pipelines.
    """

    print(production_score(sample))