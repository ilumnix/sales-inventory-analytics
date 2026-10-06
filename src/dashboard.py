import streamlit as st
import pandas as pd
from analysis import (
    get_connection,
    get_top_selling_products,
    get_most_profitable_products,
    get_low_stock_products,
    get_cheapest_suppliers,
)

st.set_page_config(page_title="Sales and Inventory Dashboard", layout="wide")

conn = get_connection()

st.title("Sales and Inventory Analytics Dashboard")
st.caption("A small-business analytics tool built with Python, SQLite, pandas, and Streamlit.")


# KPI summary
col1, col2, col3 = st.columns(3)

customers_count = pd.read_sql_query("SELECT COUNT(*) AS n FROM customers", conn)["n"][0]
orders_count = pd.read_sql_query("SELECT COUNT(*) AS n FROM orders", conn)["n"][0]
revenue = pd.read_sql_query("SELECT SUM(quantity * price_at_order) AS total FROM order_items", conn)["total"][0]

col1.metric("Total Customers", customers_count)
col2.metric("Total Orders", orders_count)
col3.metric("Total Revenue", f"${revenue:,.2f}")

st.divider()

# Top Selling
st.subheader("Top Selling Products")
top_selling = get_top_selling_products(conn)
col_a, col_b = st.columns([2, 1])
col_a.bar_chart(top_selling.set_index("name")["total_sold"])
col_b.dataframe(top_selling, use_container_width=True)

# Most Profitable
st.subheader("Most Profitable Products")
profit = get_most_profitable_products(conn)
col_a, col_b = st.columns([2, 1])
col_a.bar_chart(profit.set_index("name")["total_profit"])
col_b.dataframe(profit, use_container_width=True)

# Low Stock
st.subheader("Low Stock Products")
low_stock = get_low_stock_products(conn)
if low_stock.empty:
    st.success("No products are currently low on stock.")
else:
    st.warning(f"{len(low_stock)} product(s) need restocking.")
    st.dataframe(low_stock, use_container_width=True)
    
    
    # Cheapest Supplier per product
st.subheader("Cheapest Supplier per Product")
cheapest = get_cheapest_suppliers(conn)
st.dataframe(cheapest, use_container_width=True)

conn.close()