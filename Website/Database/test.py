import psycopg2

conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres")
cursor = conn.cursor()

with open("/Users/erikjunkers/Documents/TDA257/DAT257-Group11/Website/Database/tables.sql") as tables:
    query = tables.read()
    cursor.execute(query)
    conn.commit()