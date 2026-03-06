import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from src.embedding_model import create_or_load_embeddings


class AIDestinationRecommender:

    def __init__(self, df):

        # Remove duplicate destinations first
        self.df = df.drop_duplicates(subset=["Site Name"]).reset_index(drop=True)

        # Load embeddings
        self.embeddings = create_or_load_embeddings(self.df)

        # Load embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")


    def recommend(self, user_query, top_n=10):

        # Convert user query into embedding
        user_embedding = self.model.encode([user_query])

        # Calculate similarity with all destinations
        similarity_scores = cosine_similarity(
            user_embedding,
            self.embeddings
        )[0]

        # Add similarity column
        self.df["similarity"] = similarity_scores

        # Sort by similarity
        results = self.df.sort_values(
            by="similarity",
            ascending=False
        )

        # Remove duplicates again (extra safety)
        results = results.drop_duplicates(subset=["Site Name"])

        # Return top destinations
        return results.head(top_n)