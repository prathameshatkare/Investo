import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ben123",
    database="ap"
)

print("Connected to the database!")
connection.close()
