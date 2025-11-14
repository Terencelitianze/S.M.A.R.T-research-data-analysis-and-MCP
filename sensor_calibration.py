import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mysql.connector
from datetime import datetime, timedelta

# Define metadata IDs for Sensor 01
sensor_01_metadata = {
    "temperature": "all_sensor_01_temperature",  # metadata_ids[24]
    "humidity": "all_sensor_01_humidity",        # metadata_ids[25]
    "pm2_5": "all_sensor_01_pm_2_5",            # metadata_ids[29]
    "co2": "all_sensor_01_co2"                  # metadata_ids[32]
}

# Function to connect to the MySQL database
def make_db_connection():
    host = "192.168.50.200"
    port = 3306
    user = "smart_intern"
    password = "smart_intern"
    database = "sensors_database"
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor(dictionary=True)
    return connection, cursor

# Function to fetch raw data from the database
def fetch_raw_data(cursor, entity_name, start_date, end_date):
    query = """
    SELECT d.last_updated_ts, d.state
    FROM states d
    JOIN states_meta a ON d.metadata_id = a.metadata_id
    WHERE a.entity_id = %s COLLATE utf8mb4_unicode_ci
    AND last_updated_ts >= %s AND last_updated_ts < %s
    """
    cursor.execute(query, (entity_name, start_date.timestamp(), end_date.timestamp()))
    rows = cursor.fetchall()
    
    raw_data = pd.DataFrame(rows)
    
    if len(raw_data) > 0:
        # Remove non-numeric values from 'state' column
        raw_data['state'] = pd.to_numeric(raw_data['state'], errors='coerce')
        raw_data = raw_data.dropna(subset=['state'])
        # Convert 'last_updated_ts' to datetime
        raw_data['timestamp'] = pd.to_datetime(raw_data['last_updated_ts'], unit='s')
    
    return raw_data

# Define the time range
start_datetime = pd.to_datetime("2025-02-10 18:00:00")
end_datetime = pd.to_datetime("2025-02-12 16:00:00")

# Use the predefined time range
start_time = start_datetime
end_time = end_datetime

# Connect to the database
connection, cursor = make_db_connection()

# Fetch data for each sensor type
sensor_01_data = {}
for key, entity_name in sensor_01_metadata.items():
    sensor_01_data[key] = fetch_raw_data(cursor, entity_name, start_time, end_time)

# Close the database connection
cursor.close()
connection.close()

# Combine all sensor data into a single DataFrame
combined_data = None
for key, df in sensor_01_data.items():
    if not df.empty:
        df = df.rename(columns={'state': key})  # Rename 'state' column to match sensor type
        df = df[['timestamp', key]]  # Keep only relevant columns
        if combined_data is None:
            combined_data = df
        else:
            combined_data = pd.merge(combined_data, df, on='timestamp', how='outer')

# Sort the combined data by timestamp
if combined_data is not None:
    combined_data = combined_data.sort_values(by='timestamp').reset_index(drop=True)

# Display the combined data
print("Combined Sensor 01 Data:")
print(combined_data)

if combined_data is not None:
    combined_data.to_csv("sensor_01_data.csv", index=False)