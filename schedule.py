# script to insert data into FastAPI database on schedule.
# connect to redis in AWS, and insert new data into Pastgres

import psycopg2

connection = psycopg2.connect(database="api_db", user='pug', password='magician', host="localhost", port=5432)

cursor = connection.cursor()

sql_context ="""
select 
    email
from 
    public.users
"""


cursor.execute(sql_context)

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)