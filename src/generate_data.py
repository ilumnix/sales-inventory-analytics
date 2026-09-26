from faker import Faker #Imports faker class from the library
import random

import csv
fake = Faker() # creates the faker generator that will reuse for every fake value

from datetime import timedelta

# A function that takes one input (how many fake customers to generate)
# and returns that list of fake customers  
def generate_customers(n:int):
    customers = []
    
    for i in range(1, n+1):
        customer = {
            "customer_id":i,
            "name":fake.name(),
            "email":fake.email(),
            "contact_number": fake.phone_number()
        }
        
        customers.append(customer)
        
    return customers



        
        
def generate_products(n:int):
    products = []
    
    for i in range (1, n+1):
        product = {
            "product_id": i,
            "name": random.choice([
                "Laptop",
                "Wireless Mouse",
                "Mechanical Keyboard",
                "USB-C Cable",
                "Monitor",
                "Webcam",
                "Headphones",
                "Bluetooth Speaker",
                "Phone Charger",
                "Power Bank",
                "Smartphone",
                "Tablet",
                "Smartwatch",
                "Gaming Controller",
                "External Hard Drive",
                "USB Flash Drive",
                "Desk Lamp",
                "Office Chair",
                "Backpack",
                "Water Bottle",
                "Coffee Mug",
                "Notebook",
                "Pen Set",
                "Calculator",
                "Desk Organizer",
                "Keyboard Wrist Rest",
                "Mouse Pad",
                "Laptop Stand",
                "Phone Stand",
                "LED Light Strip",
                "Portable Fan",
                "Alarm Clock",
                "Digital Camera",
                "Tripod",
                "Microphone",
                "Printer",
                "Scanner",
                "HDMI Cable",
                "Ethernet Cable",
                "Surge Protector",
                "Extension Cord",
                "Desk Mat",
                "Whiteboard",
                "Sticky Notes",
                "Stapler",
                "Scissors",
                "Backpack Organizer",
                "Travel Adapter",
                "Mini Projector",
                "Air Purifier"
            ]),
            "serial_number": fake.bothify(text="???#######"),
            "stock_quantity": random.randint(0,100),
            "price": round(random.uniform(10 , 1000) , 2),
        }
        products.append(product)
    
    return products


def generate_orders(customers, n:int):
    orders = []
    for i in range (1, n+1):
        temp = random.choice(customers)
        
        order = {
            "order_id":i,
            "customer_id": temp["customer_id"],
            "order_date": fake.date_this_year()
        
        }
        orders.append(order)
        
    return orders
    
def generate_order_items(orders, products):
    
    order_items = []
    counter = 0
    
    for o in orders:
        
        
        order_item_count = random.randint(2,5)
        
        for i in range (1 , order_item_count):      
            counter+=1 
            temp = random.choice(products)          
            order_item ={
                "order_item_id": counter,
                "order_id": o["order_id"],
                "product_id":  temp["product_id"],
                "price_at_order": temp["price"],
                "quantity": random.randint(1,4),
                "shipping_date" : o["order_date"] + timedelta(days=random.randint(3, 30))
            }
            order_items.append(order_item)
        
    return order_items

def generate_suppliers(n:int):
    suppliers = []
    for i in range (1, n+1):
        supplier = {
            "supplier_id":i,
            "name":fake.company(),
            
        }
        suppliers.append(supplier)
    return suppliers


def generate_supplies(suppliers, n:int, products):
    supplies = []
    
    for i in range (1, n+1):
        temp_s = random.choice(suppliers)
        temp_p = random.choice(products)
        supply = {
            "supply_id": i  ,
            "supplier_id":temp_s["supplier_id"],
            "product_id": temp_p["product_id"],
            "cost_per_unit": round(temp_p["price"] * random.uniform(0.4, 0.7), 2),
            "quantity": random.randint(20,100),
            "arrival_date": fake.date_this_year() ,
        }    
        supplies.append(supply)
    return supplies
    
def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8")as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":

    customers = generate_customers(60)
    products = generate_products(40)
    orders = generate_orders(customers, 180)
    order_items = generate_order_items(orders, products)
    suppliers = generate_suppliers(6)
    supplies = generate_supplies(suppliers, 100, products)

    save_to_csv(customers, "data/customers.csv")
    save_to_csv(products, "data/products.csv")
    save_to_csv(orders, "data/orders.csv")
    save_to_csv(order_items, "data/order_items.csv")
    save_to_csv(suppliers, "data/suppliers.csv")
    save_to_csv(supplies, "data/supplies.csv")
    
    print("All data generated and saved to data/ folder.")