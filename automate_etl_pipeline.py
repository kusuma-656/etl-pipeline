import pandas as pd
import sqlite3
import os

# Step 1: Extract - Load the raw data from a CSV file
def extract(csv_file):
    print("Extracting data from:", csv_file)
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        print("Data successfully extracted.")
        return df
    else:
        raise FileNotFoundError(f"File '{csv_file}' not found!")

# Step 2: Transform - Perform transformations on the data
def transform(df):
    print("Transforming the data...")
    # Example transformation: Adding a new column with double the score
    if 'Study_Hours_Per_Day' in df.columns:
        df['Personal_Space_Hours_Per_Day'] = df['Study_Hours_Per_Day'] * 2
        print("Transformation complete: Added 'Personal_Space_Hours_Per_Day' column.")
    else:
        print("Column 'score' not found. No transformation applied.")
    return df

# Step 3: Load - Load the transformed data into SQLite
def load(df, db_file, table_name):
    print("Loading data into SQLite database...")
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    # Load the data into a table
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Data successfully loaded into table '{table_name}' in database '{db_file}'.")
    # Verify the load
    print("\nVerifying the first 5 rows of the table:")
    result = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5;", conn)
    print(result)
    # Close the connection
    conn.close()
    print("Database connection closed.")

# Step 4: Automate the Pipeline
def run_etl_pipeline(csv_file, db_file, table_name):
    print("Starting the ETL pipeline...")
    try:
        # Extract
        raw_data = extract(csv_file)
        # Transform
        transformed_data = transform(raw_data)
        # Load
        load(transformed_data, db_file, table_name)
        print("ETL pipeline executed successfully!")
    except Exception as e:
        print("Error in ETL pipeline:", e)

# Step 5: Schedule or Trigger the Pipeline
if __name__ == "__main__":
    # Input CSV file
    input_csv = "data.csv"  # Path to the input CSV file
    # SQLite database file
    sqlite_db = "etl_pipeline.db"
    # Table name
    table_name = "transformed_table"

    # Run the ETL pipeline
    run_etl_pipeline(input_csv, sqlite_db, table_name)
