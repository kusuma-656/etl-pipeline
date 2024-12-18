import sqlite3

# Step 1: Create a connection to the SQLite database (or create a new one)
db_path = "etl_pipeline.db"  # Name of the SQLite database file
conn = sqlite3.connect(db_path)

print("Database connected successfully!")

import pandas as pd

# Step 2: Load the transformed data from CSV into a pandas DataFrame
csv_path = "transformed_data.csv"  # Path to your transformed CSV file
df = pd.read_csv(csv_path)

print("Transformed Data Loaded into DataFrame:")
print(df.head())

# Step 3: Load the DataFrame into SQLite
table_name = "transformed_table"  # Name of the table in SQLite

df.to_sql(table_name, conn, if_exists="replace", index=False)

print(f"Data successfully loaded into SQLite table '{table_name}'.")

# Step 4: Verify the data in the SQLite table
query = f"SELECT * FROM {table_name} LIMIT 5;"  # Query to fetch the first 5 rows
result = pd.read_sql(query, conn)

print("First 5 Rows from the SQLite Table:")
print(result)

# 2.1: Query to count the number of rows in the table
query_count = "SELECT COUNT(*) FROM transformed_table;"
result_count = pd.read_sql(query_count, conn)
print("\nTotal Number of Rows in the Table:")
print(result_count)

# 2.2: Query to fetch rows where 'score' > 50
query_score = "SELECT * FROM transformed_table WHERE Study_Hours_Per_Day > 5;"
result_score = pd.read_sql(query_score, conn)
print("\nRows Where 'score' > 50:")
print(result_score)

# 2.3: Query to calculate the average of the 'Study_Hours_Per_Day' column
query_avg = "SELECT AVG(Study_Hours_Per_Day) FROM transformed_table;"
result_avg = pd.read_sql(query_avg, conn)
print("\nAverage of 'score' Column:")
print(result_avg)

conn.close()
print("Database connection closed.")