import random
import csv

# Define sample data
customers = []
orders = []

# Sample customer names
customer_names = ["John", "Jane", "Michael", "Emily", "David", "Olivia"]

# Sample product categories
product_categories = ["Fruits", "Vegetables", "Dairy", "Meat", "Bakery"]

# Generate additional sample data
for i in range(1, 10001):
    customer = {
        "id": i,
        "name": random.choice(customer_names),
        "email": f"customer{i}@example.com",
        "phone": f"{random.randint(1000000000, 9999999999)}",
    }
    customers.append(customer)

    order = {
        "id": i,
        "customer_id": i,
        "product": f"{random.choice(product_categories)} {i}",
        "quantity": random.randint(1, 10),
        "price": round(random.uniform(1.0, 100.0), 2),
    }
    orders.append(order)

customer_fieldnames = ["id", "name", "email", "phone"]
order_fieldnames = ["id", "customer_id", "product", "quantity", "price"]

with open("customer.csv", "w", newline="") as customer_file:
    customer_writer = csv.DictWriter(customer_file, fieldnames=customer_fieldnames)
    customer_writer.writeheader()
    customer_writer.writerows(customers)

with open("orders.csv", "w", newline="") as order_file:
    order_writer = csv.DictWriter(order_file, fieldnames=order_fieldnames)
    order_writer.writeheader()
    order_writer.writerows(orders)

print("Data saved to customer.csv and orders.csv")
