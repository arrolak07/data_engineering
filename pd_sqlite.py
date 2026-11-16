# MINI PROJECT:
import sqlite3
import pandas as pd

conn = sqlite3.connect("shop.db")

# 1. READ THE CSV JSON AND EXCEL FILE (INGEST)
sales = pd.read_csv("sales.csv")
customers = pd.read_json("customers.json")
products = pd.read_excel("products.xlsx")
# TOP 5
print(sales.head(),"\n")
# Number of rows before cleaning
print("Number of Sales Data rows before cleaning:",len(sales))

# 2. RAW DATA TO SQLITE
sales.to_sql("raw_sales", conn, if_exists="replace", index=False)
customers.to_sql("raw_customers", conn, if_exists="replace", index=False)
products.to_sql("raw_products", conn, if_exists="replace", index=False)
print("RAW TABLES ARE IN SQLITE")

# 3. READ FROM SQLITE
sales = pd.read_sql_query("SELECT * FROM raw_sales", conn)
customers = pd.read_sql_query("SELECT * FROM raw_customers", conn)
products = pd.read_sql_query("SELECT * FROM raw_products", conn)

# 4. CLEANING DATA

sales = sales.drop_duplicates() # Remove duplicates
sales["quantity"] = sales["quantity"].fillna(1) # Filling Missed quantity with 1
sales["status"] = sales["status"].str.lower()
sales["order_date"] = pd.to_datetime(sales["order_date"])
customers["city"] = customers["city"].fillna("Unknown")

# number of rows after cleaning
print("Number of Customer Data rows After cleaning:",len(customers))
print(customers)

# 5. TRANSFORM
data = sales.merge(customers, on="customer_id")
data = data.merge(products, on="product_id")
data = data[data["status"] == "completed"]  # Keeping only completed orders

# NEW COLUMNS
data["Revenue"] = data["quantity"] * data["price"]
data["month"] = data["order_date"].dt.strftime("%Y-%m")

# Summaries
sales_by_month = data.groupby("month")["Revenue"].sum().reset_index()
print(sales_by_month)
sales_by_category = data.groupby("category")["Revenue"].sum().reset_index()
print(sales_by_category)
sales_by_customer = data.groupby("name")["Revenue"].sum().reset_index()
print(sales_by_customer)
# sorting the customers revenue by desc by giving asc = False
sales_by_customer = sales_by_customer.sort_values("Revenue", ascending = False)
print(sales_by_customer)
# Only Top 5 customers
top_sales_by_customer = sales_by_customer.head(5)
print(top_sales_by_customer)

print(sales_by_month)
print(sales_by_category)

# 6. SAVE THE CURATED DATA TO SQLITE
data["order_date"] = data["order_date"].dt.strftime("%Y-%m-%d")
data.to_sql("curated_sales", conn, if_exists="replace", index=False)
sales_by_month.to_sql("sales_by_month", conn, if_exists="replace", index=False)
sales_by_category.to_sql("sales_by_category", conn, if_exists="replace", index=False)
sales_by_customer.to_sql("sales_by_customer", conn, if_exists="replace", index=False)

conn.close()
print("Done! Curated tables saved in shop.db")

