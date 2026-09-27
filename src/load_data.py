import csv
import sqlite3


conn = sqlite3.connect("database/sales.db")
cursor = conn.cursor()

def load_customers(cursor):
    with open("data/customers.csv", "r") as f:
        reader = csv.DictReader(f)
        rows_insert = []
        for row in reader:
            row_append = (int(row["customer_id"]), row["name"], row["email"], row["contact_number"])
            rows_insert.append(row_append)
            
    
    cursor.executemany(
        "INSERT INTO customers (customer_id, name, email, contact_number) VALUES (?, ?, ?, ?)",
        rows_insert
    )
            


def load_products(cursor):
    with open("data/products.csv", "r") as f:
        reader = csv.DictReader(f)
        rows_insert = []
        for row in reader:
            row_append = (int(row["product_id"]), row["name"], row["serial_number"], int(row["stock_quantity"]), float(row["price"]))
            rows_insert.append(row_append)
            
    
    cursor.executemany(
        "INSERT INTO products (product_id,name,serial_number,stock_quantity,price) VALUES (?, ?, ?, ?, ?)",
        rows_insert
    )



def load_orders(cursor):
    with open("data/orders.csv", "r") as f:
        reader = csv.DictReader(f)
        rows_insert = []
        for row in reader:
            row_append = (int(row["order_id"]), int(row["customer_id"]), row["order_date"])
            rows_insert.append(row_append)

    cursor.executemany(
        "INSERT INTO orders (order_id, customer_id, order_date) VALUES (?, ?, ?)",
        rows_insert
    )


def load_order_items(cursor):
    with open("data/order_items.csv", "r") as f:
        reader = csv.DictReader(f)
        rows_insert = []
        for row in reader:
            row_append = (
                int(row["order_item_id"]),
                int(row["order_id"]),
                int(row["product_id"]),
                float(row["price_at_order"]),
                int(row["quantity"]),
                row["shipping_date"]
            )
            rows_insert.append(row_append)

    cursor.executemany(
        "INSERT INTO order_items (order_item_id, order_id, product_id, price_at_order, quantity, shipping_date) VALUES (?, ?, ?, ?, ?, ?)",
        rows_insert
    )


def load_suppliers(cursor):
    with open("data/suppliers.csv", "r") as f:
        reader = csv.DictReader(f)
        rows_insert = []
        for row in reader:
            row_append = (int(row["supplier_id"]), row["name"])
            rows_insert.append(row_append)

    cursor.executemany(
        "INSERT INTO suppliers (supplier_id, name) VALUES (?, ?)",
        rows_insert
    )


def load_supplies(cursor):
    with open("data/supplies.csv", "r") as f:
        reader = csv.DictReader(f)
        rows_insert = []
        for row in reader:
            row_append = (
                int(row["supply_id"]),
                int(row["supplier_id"]),
                int(row["product_id"]),
                float(row["cost_per_unit"]),
                int(row["quantity"]),
                row["arrival_date"]
            )
            rows_insert.append(row_append)

    cursor.executemany(
        "INSERT INTO supplies (supply_id, supplier_id, product_id, cost_per_unit, quantity, arrival_date) VALUES (?, ?, ?, ?, ?, ?)",
        rows_insert
    )


load_customers(cursor)
load_products(cursor)
load_orders(cursor)
load_order_items(cursor)
load_suppliers(cursor)
load_supplies(cursor)





conn.commit()
conn.close()


print("loading data done")