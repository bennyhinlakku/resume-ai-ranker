from pathlib import Path
from docx import Document
import re

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JD_FILE = PROJECT_ROOT / "data" / "job_description.docx"


class JDParser:

    def __init__(self):
        self.text = self.load_jd().lower()

    def load_jd(self):
        doc = Document(JD_FILE)
        return "\n".join(p.text for p in doc.paragraphs)

    def extract_experience(self):
        match = re.search(r'(\d+)\s*[-–]\s*(\d+)\s*years', self.text)

        if match:
            return {
                "min": int(match.group(1)),
                "max": int(match.group(2))
            }

        return None

    def extract_locations(self):

        cities = [
            "pune",
            "noida",
            "hyderabad",
            "mumbai",
            "delhi"
        ]

        return [c for c in cities if c in self.text]

    def extract_keywords(self):

        keywords = [
            "python",
            "retrieval",
            "ranking",
            "embeddings",
            "milvus",
            "pinecone",
            "faiss",
            "weaviate",
            "qdrant",
            "elasticsearch",
            "opensearch",
            "llm",
            "fine-tuning",
            "lora",
            "qlora",
            "peft",
            "ndcg",
            "mrr",
            "map",
            "a/b testing",
            "hybrid search",
            "sentence-transformers",
            "vector database"
        ]

        return [k for k in keywords if k in self.text]


if __name__ == "__main__":

    parser = JDParser()

    print("=" * 60)
    print("Experience")
    print(parser.extract_experience())

    print("\nLocations")
    print(parser.extract_locations())

    print("\nKeywords")
    print(parser.extract_keywords())
    print("=" * 60)