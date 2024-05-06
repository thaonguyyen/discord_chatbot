import requests
import psycopg2
import json
from datetime import datetime
import time
import schedule

def fetch_data():
    url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"
    try:
        # get response from api
        response = requests.get(url)
        return response.json()
    # error fetching data
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def write_to_db(data):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="api",
            user="postgres",
            host="localhost"
        )
        # write api call response into table
        cursor = conn.cursor()
        cursor.execute("INSERT INTO api_data (data) VALUES (%s)", (json.dumps(data),))
        conn.commit()
        cursor.close()
    # error writing to table
    except psycopg2.DatabaseError as e:
        print(f"Error writing to database: {e}")
    finally:
        if conn is not None:
            conn.close()

def job():
    # scheduled fetching
    data = fetch_data()
    if data is not None:
        write_to_db(data)
    print(f"Data fetched and written to database at {datetime.now()}")

job_count = {"count": 0}

def scheduled_job():
    # schedule data call every minute
    if job_count["count"] < 60:
        job()
        job_count["count"] += 1
    else:
        print("Successfully completed 60 executions")
        schedule.clear()

schedule.every(1).minute.do(scheduled_job)

# run scheduling
if __name__ == "__main__":
    try:
        while schedule.get_jobs():
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped by user.")
