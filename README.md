Product Deduplication - Veridion Challenge

I chose task number #4  Product Deduplication

1.	Task Overview
The goal of this task is to consolidate duplicate entries in a product dataset, ensuring that each product is represented by a single, enriched entry that maximizes
 available information while ensuring uniqueness.

3.	Approach
I chose to resolve this challenge by testing two methods: 
•	the TF-IDF(Term Frequency - Inverse Document Frequency)  method 
•	the Embeddings method.

Both methods proved effective in identifying and consolidating duplicate products, but the TF-IDF method stands out in terms of execution speed.
While embeddings can provide a deeper understanding of semantic relationships between product titles, TF-IDF offers a faster, computationally less expensive solution, and in this case,
the clustering results were quite similar, with only marginal differences in the accuracy of the deduplication process.
In order to process the data, I converted the file into a CSV format, and the resulting files were also saved as CSV files.
I applied clustering and adjusted the epsilon (eps) parameter to achieve the most accurate results. The first value I tested for both methods was 0.5, but the results were unsatisfactory.
The second value was 0.3, and the final value used was 0.2, which provided the best outcomes.
Assigned each product a cluster ID, with -1 indicating noise (unclustered items). I compared the first 20 entries in the file for both methods. 

5.	The steps I followed to create the program
I installed the necessary dependencies and wrote the code for the first method. I reviewed the results, and then, to understand better and see if there was a better alternative, I implemented the second method.
After conducting several tests and adjusting the values, multiple CSV files were generated. In conclusion, I personally find that the first method, TF-IDF + DBSCAN,
is more efficient in terms of execution time, and the difference in the number of clusters is minimal.

7.	Project Structure
•	Untitled-1.py - Used for converting the Parquet file to CSV so it can be opened. I imported the pandas library for this.
import pandas as pd
•	deduplication_embeddings.py- Used for the embeddings method.
•	deduplication.py - Used for implementing the TF-IDF method.
•	The final CSV files for the two methods are output_tfidf.csv for the first method, and deduplicated_products_embeddings3.csv for the embeddings method.

