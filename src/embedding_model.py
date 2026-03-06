import os
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

MODEL_PATH = "models/destination_embeddings.npy"

model = SentenceTransformer(MODEL_NAME)


def create_or_load_embeddings(df):

    if os.path.exists(MODEL_PATH):
        print("Loading saved embeddings...")
        embeddings = np.load(MODEL_PATH)
        return embeddings

    print("Creating embeddings for the first time...")

    text_data = (
        df["Site Name"].astype(str) + " " +
        df["Type"].astype(str) + " " +
        df["city"].astype(str) + " " +
        df["country"].astype(str)
    )

    embeddings = model.encode(text_data.tolist(), show_progress_bar=True)

    np.save(MODEL_PATH, embeddings)

    return embeddings