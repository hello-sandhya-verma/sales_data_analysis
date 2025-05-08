import pandas as pd
import matplotlib.pyplot as plt

# Sample e-commerce data
data = {
    'Product ID': ['P001', 'P002', 'P003', 'P001', 'P004'],
    'Product Name': ['Laptop', 'Headphones', 'T-shirt', 'Laptop', 'Coffee Maker'],
    'Customer ID': ['C001', 'C002', 'C003', 'C004', 'C005'],
    'Order Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Electronics', 'Kitchen'],
    'Quantity': [2, 1, 3, 1, 1],
    'Price': [500, 50, 20, 500, 80],
    'Discount': [0.1, 0.05, 0.0, 0.1, 0.15]
}

# Create DataFrame
df = pd.DataFrame(data)

# Data cleaning and adding Total Sales column
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Total Sales'] = df['Quantity'] * df['Price'] * (1 - df['Discount'])
df['Month'] = df['Order Date'].dt.to_period('M')

# Pivot Tables for Analysis
product_performance = pd.pivot_table(df, values=['Total Sales', 'Quantity'], index='Product Name', aggfunc={'Total Sales': 'sum', 'Quantity': 'sum'})
category_performance = pd.pivot_table(df, values='Total Sales', index='Category', aggfunc='sum')
customer_performance = pd.pivot_table(df, values='Total Sales', index='Customer ID', aggfunc='sum')
monthly_sales = pd.pivot_table(df, values='Total Sales', index='Month', aggfunc='sum')

# Displaying Insights

# Product Performance
top_products = product_performance.sort_values(by='Total Sales', ascending=False).head(3)
print("\n=== Top Products by Sales ===")
for index, row in top_products.iterrows():
    print(f"Product: {index} | Total Sales: ${row['Total Sales']:.2f} | Quantity Sold: {row['Quantity']}")

# Category Performance
top_categories = category_performance.sort_values(by='Total Sales', ascending=False).head(3)
print("\n=== Top Categories by Sales ===")
for index, row in top_categories.iterrows():
    print(f"Category: {index} | Total Sales: ${row['Total Sales']:.2f}")

# Customer Performance
top_customers = customer_performance.sort_values(by='Total Sales', ascending=False).head(3)
print("\n=== Top Customers ===")
for index, row in top_customers.iterrows():
    print(f"Customer ID: {index} | Total Sales: ${row['Total Sales']:.2f}")

# Monthly Sales Trends
print("\n=== Monthly Sales Trends ===")
for period, row in monthly_sales.iterrows():
    print(f"Month: {period} | Total Sales: ${row['Total Sales']:.2f}")

# Step 5: Data Visualization

# 1. Bar Chart for Product Performance (Top 3 Products)
plt.figure(figsize=(10, 6))
top_products['Total Sales'].plot(kind='bar', color='skyblue')
plt.title('Top 3 Products by Sales', fontsize=14)
plt.xlabel('Product Name', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)

# Fix for identical xlims warning: set xlim to allow for spacing
if len(top_products) > 1:  # Ensure more than one data point exists
    plt.xlim(-0.5, len(top_products) - 0.5)

plt.tight_layout()
plt.show()

# 2. Bar Chart for Category Performance (Top 3 Categories)
plt.figure(figsize=(10, 6))
top_categories['Total Sales'].plot(kind='bar', color='lightgreen')
plt.title('Top 3 Categories by Sales', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)

# Fix for identical xlims warning: set xlim to allow for spacing
if len(top_categories) > 1:
    plt.xlim(-0.5, len(top_categories) - 0.5)

plt.tight_layout()
plt.show()

# 3. Pie Chart for Customer Contribution (Top 3 Customers)
plt.figure(figsize=(8, 8))
top_customers['Total Sales'].plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Top 3 Customers Contribution to Total Sales', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.show()

# 4. Line Chart for Monthly Sales Trends
plt.figure(figsize=(10, 6))
monthly_sales['Total Sales'].plot(kind='line', marker='o', color='orange')
plt.title('Monthly Sales Trends', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)

# Fix for identical xlims warning: set xlim to allow for spacing
if len(monthly_sales) > 1:
    plt.xlim(-0.5, len(monthly_sales) - 0.5)

plt.tight_layout()
plt.show()
