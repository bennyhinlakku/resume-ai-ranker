from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class Embedder:
    """
    Generates semantic embeddings and computes similarity.
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        print("Model loaded successfully.\n")

    def embed(self, text):
        """
        Convert text into an embedding vector.
        """
        return self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def similarity(self, text1, text2):
        """
        Compute cosine similarity between two texts.
        """
        emb1 = self.embed(text1)
        emb2 = self.embed(text2)

        score = cosine_similarity(
            emb1.reshape(1, -1),
            emb2.reshape(1, -1)
        )[0][0]

        return float(score)


if __name__ == "__main__":

    embedder = Embedder()

    job = """
    Senior AI Engineer with experience in retrieval,
    embeddings, ranking systems, Python,
    vector databases and LLMs.
    """

    candidate = """
    Backend Engineer with experience building
    semantic search systems using Milvus,
    embeddings, Python and retrieval pipelines.
    """

    score = embedder.similarity(job, candidate)

    print("=" * 50)
    print("Semantic Similarity Score")
    print("=" * 50)
    print(score)