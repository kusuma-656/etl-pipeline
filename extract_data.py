# Import the pandas library
import pandas as pd

# Step 1: Define the path to your CSV file
file_path = 'data.csv'  # Replace with the correct path to your dataset

# Step 2: Load the CSV file into a DataFrame
try:
    df = pd.read_csv(file_path)
    print("Data Loaded Successfully!")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit()

# Step 3: Display the first 5 rows of the dataset
print("First 5 Rows of the Dataset:")
print(df.head())

# Step 4: Print basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Step 5: Print summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

print(df.columns)  # Show column names
print(df.shape)    # Show number of rows and columns
