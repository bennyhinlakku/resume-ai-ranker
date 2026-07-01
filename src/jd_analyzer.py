from pathlib import Path
from docx import Document
import re

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JOB_FILE = PROJECT_ROOT / "data" / "job_description.docx"


def load_job_description(path):
    doc = Document(path)

    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text)

    return "\n".join(text)


def analyze_jd(text):

    text_lower = text.lower()

    analysis = {}

    # ----------------------------------
    # Experience
    # ----------------------------------

    match = re.search(
        r'(\d+)\s*[-–]\s*(\d+)\s*years',
        text_lower
    )

    if match:
        analysis["experience"] = {
            "min": int(match.group(1)),
            "max": int(match.group(2))
        }

    # ----------------------------------
    # Locations
    # ----------------------------------

    cities = [
        "pune",
        "noida",
        "hyderabad",
        "mumbai",
        "delhi"
    ]

    analysis["locations"] = [
        city
        for city in cities
        if city in text_lower
    ]

    # ----------------------------------
    # Must Have Skills
    # ----------------------------------

    must_have = [
        "python",
        "embeddings",
        "retrieval",
        "ranking",
        "milvus",
        "pinecone",
        "faiss",
        "weaviate",
        "qdrant",
        "elasticsearch",
        "opensearch",
        "llm",
        "evaluation",
        "ndcg",
        "mrr",
        "map"
    ]

    analysis["must_have"] = [
        skill
        for skill in must_have
        if skill in text_lower
    ]

    # ----------------------------------
    # Good To Have
    # ----------------------------------

    good_to_have = [
        "lora",
        "qlora",
        "peft",
        "marketplace",
        "hr-tech",
        "distributed systems",
        "open source"
    ]

    analysis["good_to_have"] = [
        item
        for item in good_to_have
        if item in text_lower
    ]

    # ----------------------------------
    # Disqualifiers
    # ----------------------------------

    analysis["avoid"] = [
        "research only",
        "langchain only",
        "consulting only",
        "computer vision only",
        "speech only",
        "robotics only"
    ]

    # ----------------------------------
    # Behavioral Expectations
    # ----------------------------------

    analysis["behavior"] = [
        "ship fast",
        "mentor",
        "product thinking",
        "production mindset",
        "writes code"
    ]

    return analysis


if __name__ == "__main__":

    jd = load_job_description(JOB_FILE)

    result = analyze_jd(jd)

    print("=" * 60)

    for key, value in result.items():
        print(f"\n{key}")
        print(value)

    print("\n" + "=" * 60)