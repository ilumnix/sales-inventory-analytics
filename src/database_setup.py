import sqlite3


conn = sqlite3.connect("database/sales.db")
cursor = conn.cursor()

with open("database/schema.sql", "r") as f:
    schema_sql = f.read()
    
cursor.executescript(schema_sql)


conn.commit()
conn.close()


print("database done")