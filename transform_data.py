import pandas as pd

# Load the dataset
file_path = 'data.csv'  # Replace with the path to your CSV
df = pd.read_csv(file_path)

print("Data Before Transformation:")
print(df.head())  # Preview the data

# Filter rows where 'Study_Hours_Per_Day' column is greater than 40
filtered_df = df[df['Study_Hours_Per_Day'] > 5]

print("Filtered Data (value > 40):")
print(filtered_df)

# Drop rows with missing values
cleaned_df = df.dropna()

print("Data After Dropping Missing Values:")
print(cleaned_df)

# Replace missing values in the 'Study_Hours_Per_Day' column with 0
df['value'] = df['Study_Hours_Per_Day'].fillna(0)

print("Data After Filling Missing Values:")
print(df)

# Rename 'Extracurricular_Hours_Per_Day' column to 'Enjoyable_Hours_Per_Day'
df = df.rename(columns={'Extracurricular_Hours_Per_Day': 'Enjoyable_Hours_Per_Day'})

print("Data After Renaming Columns:")
print(df.head())

# Drop the 'Physical_Activity_Hours_Per_Day' column
df = df.drop(columns=['Physical_Activity_Hours_Per_Day'])

print("Data After Dropping 'name' Column:")
print(df.head())

# Calculate the sum of 'Sleep_Hours_Per_Day' column
total_score = df['Sleep_Hours_Per_Day'].sum()

print(f"Total Score: {total_score}")

# Group by 'Student_ID' column and calculate the mean of 'Study_Hours_Per_Day'
grouped_df = df.groupby('Student_ID')['Study_Hours_Per_Day'].mean()

print("Grouped Data (Average Score per ID):")
print(grouped_df)

# Create a new column 'Personal_Space_Hours_Per_Day' by multiplying 'Study_Hours_Per_Day' by 2
df['Personal_Space_Hours_Per_Day'] = df['Study_Hours_Per_Day'] * 2

print("Data After Adding 'double_score' Column:")
print(df.head())

# Sort by 'Study_Hours_Per_Day' in descending order
sorted_df = df.sort_values(by='Study_Hours_Per_Day', ascending=False)

print("Data Sorted by 'score' in Descending Order:")
print(sorted_df)

sorted_df.to_csv('transformed_data.csv', index=False)
print("\nTransformed Data Saved to 'transformed_data.csv'")


