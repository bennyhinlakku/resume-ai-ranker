from embedder import Embedder

from feature_engineering import (
    load_candidates,
    extract_features,
    DATA_FILE
)

from jd_analyzer import (
    load_job_description,
    analyze_jd,
    JOB_FILE
)

from company_analyzer import analyze_company_history
from production_detector import production_score
from retrieval_detector import retrieval_score
from leadership_detector import leadership_score


class HybridScorer:

    def __init__(self):

        self.embedder = Embedder()

        jd_text = load_job_description(JOB_FILE)

        self.jd = analyze_jd(jd_text)

    def score(self, candidate):

        total_score = 0
        breakdown = {}

        # =====================================================
        # Semantic Similarity (25)
        # =====================================================

        candidate_text = (
            candidate["headline"] + " " +
            candidate["summary"] + " " +
            candidate["career_text"]
        )

        jd_text = """
        Senior AI Engineer with production experience
        in retrieval, embeddings, ranking,
        vector databases, Python and LLM systems.
        """

        semantic = self.embedder.similarity(
            jd_text,
            candidate_text
        )

        semantic_score = semantic * 25

        total_score += semantic_score

        breakdown["semantic"] = round(semantic_score, 2)

        # =====================================================
        # Must-Have Skills (15)
        # =====================================================

        skill_score = 0

        for skill in self.jd["must_have"]:

            for candidate_skill in candidate["skills"]:

                if skill.lower() in candidate_skill:
                    skill_score += 1
                    break

        skill_score = min(skill_score, 15)

        total_score += skill_score

        breakdown["skills"] = skill_score

        # =====================================================
        # Company Analysis (10)
        # =====================================================

        company = analyze_company_history(
            candidate["companies"]
        )

        company_score = 0

        if company["product_experience"] >= 1:
            company_score += 6

        if not company["consulting_only"]:
            company_score += 4

        total_score += company_score

        breakdown["company"] = company_score

        # =====================================================
        # Production Experience (10)
        # =====================================================

        production = production_score(
            candidate["career_text"]
        )

        production_points = min(
            production["production_score"],
            10
        )

        total_score += production_points

        breakdown["production"] = production_points

        # =====================================================
        # Retrieval Experience (10)
        # =====================================================

        retrieval = retrieval_score(
            candidate["career_text"]
        )

        retrieval_points = min(
            retrieval["retrieval_score"],
            10
        )

        total_score += retrieval_points

        breakdown["retrieval"] = retrieval_points

        # =====================================================
        # Leadership (8)
        # =====================================================

        leadership = leadership_score(
            candidate["career_text"]
        )

        leadership_points = min(
            leadership["leadership_score"],
            8
        )

        total_score += leadership_points

        breakdown["leadership"] = leadership_points

        # =====================================================
        # Experience (10)
        # =====================================================

        exp = candidate["experience"]

        if 5 <= exp <= 9:
            exp_score = 10

        elif 4 <= exp < 5:
            exp_score = 7

        elif 9 < exp <= 12:
            exp_score = 8

        else:
            exp_score = 3

        total_score += exp_score

        breakdown["experience"] = exp_score

        # =====================================================
        # Behavioral Signals (7)
        # =====================================================

        behavior = 0

        if candidate["open_to_work"]:
            behavior += 2

        if candidate["github_score"] >= 7:
            behavior += 2

        if candidate["response_rate"] >= 0.40:
            behavior += 1

        if candidate["profile_complete"] >= 80:
            behavior += 2

        total_score += behavior

        breakdown["behavior"] = behavior

        # =====================================================
        # Notice Period (5)
        # =====================================================

        notice = candidate["notice_period"]

        if notice <= 30:
            notice_score = 5

        elif notice <= 60:
            notice_score = 3

        else:
            notice_score = 1

        total_score += notice_score

        breakdown["notice"] = notice_score

        # =====================================================
        # Penalties
        # =====================================================

        penalty = 0

        if company["consulting_only"]:
            penalty -= 8

        total_score += penalty

        breakdown["penalty"] = penalty

        # =====================================================
        # Final Score
        # =====================================================

        breakdown["total"] = round(total_score, 2)

        return breakdown


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    candidates = load_candidates(DATA_FILE)

    candidate = extract_features(candidates[0])

    scorer = HybridScorer()

    result = scorer.score(candidate)

    print("=" * 70)

    for key, value in result.items():
        print(f"{key}: {value}")

    print("=" * 70)