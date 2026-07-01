import json
from pathlib import Path
from collections import Counter

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "candidates.jsonl"


def load_candidates(file_path):
    candidates = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))
    return candidates


if __name__ == "__main__":

    candidates = load_candidates(DATA_FILE)

    print("=" * 60)
    print(f"Total Candidates: {len(candidates)}")
    print("=" * 60)

    experience = []

    skills = Counter()

    companies = Counter()

    for candidate in candidates:

        experience.append(
            candidate["profile"]["years_of_experience"]
        )

        companies[
            candidate["profile"]["current_company"]
        ] += 1

        for skill in candidate["skills"]:
            skills[skill["name"]] += 1

    print(f"\nAverage Experience: {sum(experience)/len(experience):.2f} years")

    print(f"Maximum Experience: {max(experience)} years")

    print(f"Minimum Experience: {min(experience)} years")

    print("\nTop 20 Skills")

    for skill, count in skills.most_common(20):
        print(f"{skill}: {count}")

    print("\nTop 10 Companies")

    for company, count in companies.most_common(10):
        print(f"{company}: {count}")