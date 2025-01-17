import pandas as pd
import mysql.connector

# Load the dataset
file_path = 'HINDALCO_1D.xlsx'
data = pd.read_excel(file_path)

# Connect to the database
connection = mysql.connector.connect(
     host="localhost",
    user="root",
    password="ben123",
    database="ap"
)
cursor = connection.cursor()

# Insert data into the database
for _, row in data.iterrows():
    cursor.execute("""
        INSERT INTO ticker_data (datetime, close, high, low, open, volume, instrument)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['datetime'], row['close'], row['high'], row['low'], row['open'], row['volume'], row['instrument']))

connection.commit()
cursor.close()
connection.close()
print("Data inserted successfully!")
