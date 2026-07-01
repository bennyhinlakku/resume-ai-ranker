import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "candidates.jsonl"


def load_candidates(file_path):
    candidates = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))
    return candidates


def build_profile(candidate):

    profile = candidate["profile"]

    text = []

    # Basic Profile
    text.append(f"Headline: {profile['headline']}")
    text.append(f"Summary: {profile['summary']}")
    text.append(f"Experience: {profile['years_of_experience']} years")
    text.append(f"Current Role: {profile['current_title']}")
    text.append(f"Industry: {profile['current_industry']}")

    # Career History
    text.append("\nCareer History:")

    for job in candidate["career_history"]:
        text.append(
            f"{job['title']} at {job['company']}: {job['description']}"
        )

    # Skills
    skills = [
        skill["name"]
        for skill in candidate["skills"]
    ]

    text.append("\nSkills:")
    text.append(", ".join(skills))

    # Education
    text.append("\nEducation:")

    for edu in candidate["education"]:
        text.append(
            f"{edu['degree']} in {edu['field_of_study']}"
        )

    # Redrob Signals
    signals = candidate["redrob_signals"]

    text.append("\nBehavior Signals:")
    text.append(
        f"GitHub Activity Score: {signals['github_activity_score']}"
    )
    text.append(
        f"Recruiter Response Rate: {signals['recruiter_response_rate']}"
    )
    text.append(
        f"Interview Completion Rate: {signals['interview_completion_rate']}"
    )

    return "\n".join(text)


if __name__ == "__main__":

    candidates = load_candidates(DATA_FILE)

    profile = build_profile(candidates[0])

    print(profile)