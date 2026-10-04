import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("database/sales.db")

TOP_SELLING_QUERY = """
SELECT p.product_id, p.name, SUM(oi.quantity) AS total_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.name
ORDER BY total_sold DESC;
"""

def get_top_selling_products(conn, limit=10):
    df = pd.read_sql_query(TOP_SELLING_QUERY, conn)
    return df.head(limit)



PROFIT_QUERY = """
SELECT p.product_id, p.name,
       SUM(oi.quantity * (oi.price_at_order - avg_cost.avg_cost)) AS total_profit
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN (
    SELECT product_id, AVG(cost_per_unit) AS avg_cost
    FROM supplies
    GROUP BY product_id
) avg_cost ON p.product_id = avg_cost.product_id
GROUP BY p.product_id, p.name
ORDER BY total_profit DESC;
"""

def get_most_profitable_products(conn, limit=10):
    df = pd.read_sql_query(PROFIT_QUERY, conn)
    return df.head(limit)


LOW_STOCK_QUERY = """
SELECT product_id, name, stock_quantity
FROM products
WHERE stock_quantity < 20
ORDER BY stock_quantity ASC;
"""

def get_low_stock_products(conn):
    return pd.read_sql_query(LOW_STOCK_QUERY, conn)



CHEAPEST_SUPPLIER_QUERY = """
SELECT p.product_id, p.name AS product_name, s.name AS supplier_name, sup.cost_per_unit
FROM supplies sup
JOIN products p ON sup.product_id = p.product_id
JOIN suppliers s ON sup.supplier_id = s.supplier_id
WHERE sup.cost_per_unit = (
    SELECT MIN(cost_per_unit)
    FROM supplies
    WHERE product_id = sup.product_id
)
ORDER BY p.name;
"""

def get_cheapest_suppliers(conn):
    return pd.read_sql_query(CHEAPEST_SUPPLIER_QUERY, conn)


if __name__ == "__main__":
    conn = get_connection()

    print("----Top Selling Products----")
    print(get_top_selling_products(conn))

    print("\n----Most Profitable Products----")
    print(get_most_profitable_products(conn))

    print("\n----Low Stock Products----")
    print(get_low_stock_products(conn))

    print("\n----Cheapest Supplier per Product----")
    print(get_cheapest_suppliers(conn))

    conn.close()