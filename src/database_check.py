import sqlite3

conn = sqlite3.connect("database/sales.db")
cursor = conn.cursor()

tables = ["customers", "products", "orders", "order_items", "suppliers", "supplies"]

for table in tables:
    print(f"--- {table} ---")
    cursor.execute(f"SELECT * FROM {table} LIMIT 5")
    for row in cursor.fetchall():
        print(row)
    print()

conn.close()