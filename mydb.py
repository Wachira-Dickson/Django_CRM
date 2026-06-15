import psycopg2

# Connect to the default postgres database
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="C0n$t@nt!n0ple",
    database="postgres"
)

conn.autocommit = True

cursor = conn.cursor()

cursor.execute("CREATE DATABASE dnowdb")

print("Database created successfully")

cursor.close()
conn.close()