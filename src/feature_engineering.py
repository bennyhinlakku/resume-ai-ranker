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


def extract_features(candidate):

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    skills = [s["name"].lower() for s in candidate["skills"]]

    career_text = " ".join(
        job["description"].lower()
        for job in candidate["career_history"]
    )

    career_titles = [
        job["title"].lower()
        for job in candidate["career_history"]
    ]

    companies = [
        job["company"]
        for job in candidate["career_history"]
    ]

    return {

        "candidate_id": candidate["candidate_id"],

        "experience": profile["years_of_experience"],

        "headline": profile["headline"],

        "summary": profile["summary"],

        "industry": profile["current_industry"],

        "current_company": profile["current_company"],

        "career_titles": career_titles,

        "companies": companies,

        "career_text": career_text,

        "skills": skills,

        "github_score": signals["github_activity_score"],

        "response_rate": signals["recruiter_response_rate"],

        "interview_rate": signals["interview_completion_rate"],

        "profile_complete": signals["profile_completeness_score"],

        "open_to_work": signals["open_to_work_flag"],

        "willing_to_relocate": signals["willing_to_relocate"],

        "notice_period": signals["notice_period_days"]
    }


if __name__ == "__main__":

    candidates = load_candidates(DATA_FILE)

    features = extract_features(candidates[0])

    print("=" * 60)

    for key, value in features.items():
        print(f"{key}: {value}")

    print("=" * 60)