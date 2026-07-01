LEADERSHIP_KEYWORDS = {
    "mentor": 3,
    "mentored": 3,
    "mentoring": 3,
    "led": 3,
    "lead": 3,
    "leading": 3,
    "managed": 2,
    "management": 2,
    "architect": 3,
    "architecture": 3,
    "ownership": 3,
    "owned": 3,
    "responsible for": 2,
    "designed": 2,
    "initiated": 2,
    "collaborated": 1,
    "cross-functional": 2,
    "decision": 1
}


def leadership_score(career_text):

    career = career_text.lower()

    score = 0
    matched = []

    for keyword, weight in LEADERSHIP_KEYWORDS.items():

        if keyword in career:
            score += weight
            matched.append(keyword)

    return {
        "leadership_score": score,
        "matched_keywords": matched
    }


if __name__ == "__main__":

    sample = """
    Led a team of engineers.
    Mentored junior developers.
    Owned the architecture of a recommendation system.
    Collaborated with cross-functional teams.
    """

    result = leadership_score(sample)

    print("=" * 60)

    for k, v in result.items():
        print(f"{k}: {v}")

    print("=" * 60)