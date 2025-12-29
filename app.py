import streamlit as st
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load model + data
model = SentenceTransformer("all-MiniLM-L6-v2")
df = pd.read_json("shots_with_embeddings.json")

# Prepare FAISS index
embedding_matrix = np.vstack(df["embedding"].tolist()).astype("float32")
index = faiss.IndexFlatIP(embedding_matrix.shape[1])
index.add(embedding_matrix)

# App title
st.title("🎬 Semantic Film Shot Search")
st.caption("Search 200+ film shots by mood, action, or concept.")

# User query input
query = st.text_input("Search for a shot", placeholder="e.g. moody long take at night")

if query:
    # Embed and search
    query_embedding = model.encode([query], normalize_embeddings=True).astype("float32")
    distances, indices = index.search(query_embedding, k=5)

    st.subheader("🔍 Results")
    for i, idx in enumerate(indices[0]):
        shot = df.iloc[idx]
        st.markdown(f"**{i+1}. {shot['Shot Title (EN)']}**")
        st.markdown(shot["Description (EN)"])
        st.markdown(f"🧠 Tags: `{', '.join(shot.get('tags', []))}`" if 'tags' in shot else "")
        st.markdown(f"**Score:** {distances[0][i]:.2f}")
        st.markdown("---")
