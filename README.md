# Project Proposal

This project implements an **ETL Pipeline** to process raw data from CSV files and store the cleaned and transformed data into a local SQLite database. The goal is to create a robust and reusable pipeline for extracting raw data, performing meaningful transformations, and storing it in a queryable format for analysis or further usage.

The pipeline was developed to explore the relationship between various lifestyle factors (e.g., study hours, sleep hours, physical activity, etc.) and student CGPA, using data from a real-world dataset.

---

# Project Description

The project uses the **"Student Lifestyle Dataset"** sourced from Kaggle to simulate a typical ETL workflow:
1. **Extracting** data from a CSV file.
2. **Transforming** the data to make it clean, readable, and ready for use.
3. **Loading** the data into an SQLite database for easy querying and future analysis.

The Python script handles all stages of the ETL process and ensures that the final database contains accurate and well-structured data for further exploration of student lifestyle habits.

---

# Finding Data

The raw data used for this project is the **"Student Lifestyle Dataset"**, sourced from Kaggle. The dataset contains lifestyle-related data for students, including fields such as study hours, sleep hours, stress levels, and CGPA. The dataset is publicly available at [Kaggle](https://www.kaggle.com/). The input CSV file has been renamed to `data.csv` for consistency.

---

# Data Cleanup and Analysis

### Dataset Fields
The dataset contains the following fields:
- **Student ID**: Unique identifier for each student.
- **Study Hours**: Number of hours spent studying each day.
- **Extracurricular Hours**: Time spent on extracurricular activities daily.
- **Sleep Hours**: Hours of sleep per day.
- **Social Hours**: Time spent socializing each day.
- **Physical Activity Hours**: Time spent on physical activities daily.
- **Stress Level**: Self-reported stress level (1 to 10 scale).
- **CGPA**: Cumulative Grade Point Average of the student.

### Transformation Steps
The transformation steps applied to the data include:
1. **Renaming Fields**: The field names were standardized for clarity and consistency:
   - `Study Hours` → `Study_Hours_Per_Day`
   - `Extracurricular Hours`, `Social Hours`, etc., remain unchanged.
   - A new derived field `Personal_Space_Hours_Per_Day` was calculated by combining non-social and personal activity time (e.g., study and sleep hours).
2. **Cleaning**: Missing or invalid entries were removed to ensure the dataset's integrity.
3. **Standardization**: All column names were formatted consistently, and data types were validated.

The Python script utilizes **pandas** for all data cleaning and transformation tasks, ensuring the pipeline is modular and easy to adapt for future requirements.

---

# Loading Steps

The transformed data is loaded into an SQLite database (`etl_pipeline.db`) using the **sqlite3** library. The steps include:
1. Establishing a connection to the local SQLite database.
2. Defining a table schema to store the transformed data.
3. Inserting the data from the pandas DataFrame into the database.

The database is stored locally, allowing for fast and efficient querying without external dependencies.

---

# Analysis / SQL Queries

Once the data is loaded into the SQLite database, the following analyses can be performed:
1. Identify students with the highest and lowest `Study_Hours_Per_Day`.
2. Find the correlation between `Stress Level` and `CGPA`.
3. Retrieve aggregated metrics like average `Study_Hours_Per_Day`, maximum `Personal_Space_Hours_Per_Day`, etc.
4. Rank students based on CGPA or any other metric of interest.

These queries can be executed using standard SQL commands in any SQLite client or directly through Python using **sqlite3**.

---

# Installation Instructions

### Prerequisites
- **Python 3.x** installed on your system.
- **pip** for installing required dependencies.

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/kusuma-656/etl-pipeline.git
