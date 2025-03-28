import pandas as pd
import re


# Deduplication using the TIF method

# Read the CSV file
df = pd.read_csv("deduplication_data.csv")

# We create the clean_text() function for text cleaning
def clean_text(text):
    if isinstance(text, str):
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'\W+', ' ', text)  # Remove special characters
        text = text.strip()  # Remove extra spaces
        return text
    return ""

# Apply the clean_text() function to the product title and description
df["clean_title"] = df["product_title"].astype(str).apply(clean_text)
df["clean_desc"] = df["description"].astype(str).apply(clean_text)

# Check the result by displaying the first few rows
print(df[["clean_title", "clean_desc"]].head())  

from sklearn.feature_extraction.text import TfidfVectorizer

# Remove common words and vectorize the titles
vectorizer = TfidfVectorizer(stop_words="english")  
tfidf_matrix = vectorizer.fit_transform(df["clean_title"])  

# Check the dimensions of the matrix to ensure the data has been processed correctly
print(tfidf_matrix.shape)  

from sklearn.cluster import DBSCAN

# Set DBSCAN parameters
dbscan = DBSCAN(eps=0.2, min_samples=2, metric="cosine")  
clusters = dbscan.fit_predict(tfidf_matrix)

# Add the cluster labels to the table
df["cluster"] = clusters  

# Display the first 20 results
print(df[["product_title", "cluster"]].head(20)) 

df.to_csv("output_tfidf.csv", index=False)
