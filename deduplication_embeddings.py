import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN


# Read the CSV file
df = pd.read_csv("deduplication_data.csv")

# Choose the column to be used for comparison
df["text_for_embedding"] = df["product_title"].astype(str) + " " + df["description"].astype(str)

# Check the data
print(df[["text_for_embedding"]].head())  

# Choose the model for embeddings
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Convert the texts into embeddings (numerical vectors)
embeddings = model.encode(df["text_for_embedding"].tolist(), convert_to_tensor=True)

# Check the dimensions of the embeddings
print(embeddings.shape)  

# Apply DBSCAN for clustering and convert the embeddings to a normal array
dbscan = DBSCAN(eps=0.2, min_samples=2, metric="cosine")
clusters = dbscan.fit_predict(embeddings.cpu().numpy())  

# Add the clustering results to the table
df["cluster"] = clusters

print(df[["product_title", "cluster"]].head(20))  

df.to_csv("deduplicated_products_embeddings3.csv", index=False)