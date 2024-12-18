import schedule
import time
from automate_etl_pipeline import run_etl_pipeline  # Import your ETL function

# Define the ETL execution function
def job():
    csv_path = "raw_data.csv"  # Path to your input CSV file
    database_path = "etl_pipeline.db"  # SQLite database path
    table_name = "transformed_table"  # The table name in the database

    # Run the ETL pipeline
    run_etl_pipeline(csv_path, database_path, table_name)
    print("ETL pipeline executed successfully!")

# Schedule the job
# This example schedules the ETL pipeline to run every day at 6:00 AM
schedule.every().day.at("06:00").do(job)

# Keep the script running
while True:
    schedule.run_pending()  # Execute any pending tasks
    time.sleep(60)  # Check every minute
