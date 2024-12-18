from apscheduler.schedulers.blocking import BlockingScheduler
from automate_etl_pipeline import run_etl_pipeline  # Import your ETL function

# Define the ETL execution function
def job():
    csv_path = "data.csv"  # Path to your input CSV file
    database_path = "etl_pipeline.db"  # SQLite database path
    table_name = "transformed_table"  # The table name in the database

    # Run the ETL pipeline
    run_etl_pipeline(csv_path, database_path, table_name)
    print("ETL pipeline executed successfully!")

# Create an instance of the scheduler
scheduler = BlockingScheduler()

# Schedule the job
# This example schedules the ETL pipeline to run every day at 6:00 AM
scheduler.add_job(job, 'cron', hour=6, minute=0)

# Start the scheduler
print("Scheduler started... ETL pipeline will run every day at 6:00 AM.")
scheduler.start()
