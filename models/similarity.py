import numpy as np

def top_k(query_embedding, embeddings, k=5):
    scores = embeddings @ query_embedding
    indices = np.argsort(scores)[::-1][:k]
    return indices, scores[indices]