import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Parameters
num_records = 1000  # Number of records to generate

# Generate Transaction Data
transaction_data = []
for _ in range(num_records):
    transaction_id = fake.uuid4()
    timestamp = fake.date_time_this_year()
    amount = round(random.uniform(5.0, 500.0), 2)  # Amount between $5 and $500
    payment_method = random.choice(['Credit Card', 'Cash', 'Debit Card', 'PayPal'])
    store_location = random.choice(['Online', 'Store A', 'Store B', 'Store C'])
    
    transaction_data.append([transaction_id, timestamp, amount, payment_method, store_location])

# Generate Customer Data
customer_data = []
for _ in range(num_records):
    customer_id = fake.uuid4()
    age = random.randint(18, 70)  # Age between 18 and 70
    gender = random.choice(['Male', 'Female'])
    income_level = random.choice(['Low', 'Medium', 'High'])
    
    purchase_history = random.sample(range(1, 101), random.randint(1, 10))  # Random previous transactions
    
    customer_data.append([customer_id, age, gender, income_level, purchase_history])

# Generate Product Data
product_data = []
for _ in range(num_records):
    product_id = fake.uuid4()
    category = random.choice(['Electronics', 'Groceries', 'Clothing', 'Home', 'Toys'])
    price = round(random.uniform(1.0, 100.0), 2)  # Price between $1 and $100
    discount = random.choice([0, round(random.uniform(5, 50), 2)])  # Discount between $0 and $50
    
    product_data.append([product_id, category, price, discount])

# Generate Behavioral Data
behavioral_data = []
for _ in range(num_records):
    browsing_history = random.sample(['page1', 'page2', 'page3', 'page4', 'page5'], random.randint(1, 3))
    cart_abandonment_rate = random.randint(0, 5)  # Number of abandoned carts
    
    behavioral_data.append([browsing_history, cart_abandonment_rate])

# Generate Anomalies and Flags
anomalies_data = []
for _ in range(num_records):
    fraud_flag = random.choice([0, 1])  # 0 = Not Fraudulent, 1 = Fraudulent
    high_risk_indicator = random.choice([0, 1])  # 0 = Low Risk, 1 = High Risk
    
    anomalies_data.append([fraud_flag, high_risk_indicator])

# Generate External Data
external_data = []
for _ in range(num_records):
    geolocation = fake.local_latlng()  # Get random lat/lng
    market_trend = random.choice(['Stable', 'Increasing', 'Decreasing'])
    
    external_data.append([geolocation, market_trend])

# Combine all data into a single DataFrame
data = pd.DataFrame(transaction_data, columns=['Transaction ID', 'Timestamp', 'Amount', 'Payment Method', 'Store Location'])
data[['Customer ID', 'Age', 'Gender', 'Income Level', 'Purchase History']] = pd.DataFrame(customer_data, index=data.index)
data[['Product ID', 'Category', 'Price', 'Discount']] = pd.DataFrame(product_data, index=data.index)
data[['Browsing History', 'Cart Abandonment Rate']] = pd.DataFrame(behavioral_data, index=data.index)
data[['Fraud Flag', 'High-Risk Indicator']] = pd.DataFrame(anomalies_data, index=data.index)
data[['Geolocation', 'Market Trend']] = pd.DataFrame(external_data, index=data.index)

# Display the first few rows of the dataset
print(data.head())