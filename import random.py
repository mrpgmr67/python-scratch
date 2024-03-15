import random
import string

# Define file names for persons, products, and sales
persons_file = 'persons.txt'
products_file = 'products.txt'
sales_file = 'sales.txt'

# Create a list to store person, product, and sale data
persons_data = []
products_data = []
sales_data = []

# Generate and store random data
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_age():
    return random.randint(18, 65)

def generate_random_price():
    return round(random.uniform(10, 1000), 2)

record_count = 1000000  # Number of records to generate

for _ in range(record_count):
    first_name = generate_random_string(5)
    last_name = generate_random_string(7)
    age = generate_random_age()
    persons_data.append(f'{first_name} {last_name}, {age}')

    product_name = generate_random_string(8)
    price = generate_random_price()
    products_data.append(f'{product_name}, {price}')

    person_id = random.randint(1, record_count // 10)  # Assuming 10 persons per sale on average
    product_id = random.randint(1, record_count // 50)  # Assuming 50 products on average
    sale_date = f'2024-01-{random.randint(1, 31)}'  # Change date format as needed
    sales_data.append(f'{person_id}, {product_id}, {sale_date}')

# Write data to text files in chunks
chunk_size = 10000  # Adjust the chunk size as needed
for i in range(0, record_count, chunk_size):
    with open(persons_file, 'a') as f:
        f.write('\n'.join(persons_data[i:i+chunk_size]) + '\n')

    with open(products_file, 'a') as f:
        f.write('\n'.join(products_data[i:i+chunk_size]) + '\n')

    with open(sales_file, 'a') as f:
        f.write('\n'.join(sales_data[i:i+chunk_size]) + '\n')

print(f"{record_count} random records saved to text files: persons.txt, products.txt, and sales.txt.")
