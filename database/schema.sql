
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name TEXT ,
    email TEXT ,
    contact_number TEXT 
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name TEXT ,
    serial_number TEXT ,
    stock_quantity INT,
    price REAL 
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    price_at_order REAL,
    quantity INT,
    shipping_date DATE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

DROP TABLE IF EXISTS suppliers;
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS supplies;
CREATE TABLE supplies (
    supply_id INT PRIMARY KEY,
    supplier_id INT,
    product_id INT,
    cost_per_unit REAL,
    quantity INT,
    arrival_date DATE,
    FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);