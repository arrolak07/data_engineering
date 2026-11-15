# MINI PROJECT ON PANDAS

import pandas as pd
# 1. READ THE CSV JSON AND EXCEL FILE
sales = pd.read_csv("sales.csv")
customers = pd.read_json("customers.json")
products = pd.read_excel("products.xlsx")
# printing the sales data
# print(sales,"\n")
# TOP 5
print(sales.head(),"\n")
# Number of rows before cleaning
print("Number of Sales Data rows before cleaning:",len(sales))


# 2. CLEANING DATA
sales = sales.drop_duplicates() # Remove duplicates
sales["quantity"] = sales["quantity"].fillna(1) # Filling Missed quantity with 1
sales["status"] = sales["status"].str.lower()
sales["order_date"] = pd.to_datetime(sales["order_date"])
customers["city"] = customers["city"].fillna("Unknown")

# number of rows after cleaning
print("Number of Customer Data rows After cleaning:",len(customers))
print(customers)

# 3. TRANSFORM
data = sales.merge(customers, on="customer_id")
data = data.merge(products, on="product_id")

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


# 4. LOADING THE DATA TO CSV
data.to_csv("clean_data.csv", index=False)
sales_by_month.to_csv("sales_by_month.csv", index=False)
sales_by_category.to_csv("sales_by_category.csv", index=False)
sales_by_customer.to_excel("sales_by_customer.xlsx", index=False)

