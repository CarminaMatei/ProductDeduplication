import pandas as pd

# Load the Parquet file
df = pd.read_parquet("veridion_product_deduplication_challenge.snappy.parquet", engine="pyarrow")

# I converted the file to CSV 
df.to_csv("deduplication_data.csv", index=False)

print("The file has been saved as deduplication_data.csv")
