import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("C:/Users/good day/Desktop/Python/Datasets/amazon_sales.csv")
print("Dataset loaded successfully!")
print(df.head())

font = {'family':'serif','color':'darkred','size':15}
font1={'family':'serif','color':'darkblue','size':20}

#data cleaning
df.dropna(inplace=True)  
df.drop_duplicates(inplace=True)  
df["Date"] = pd.to_datetime(df["Date"])
df.drop_duplicates(subset=["Order ID"], keep="last", inplace=True)

# Data Analysis
unique_products = df["Product"].unique()
print("Unique products:", unique_products)
product_vales= df["Product"].value_counts()
print("Product values:\n", product_vales)

unique_catogories = df["Category"].unique()
print("Unique categories:", unique_catogories)
catogories_values = df["Category"].value_counts()
print("Category values:\n", catogories_values)

locations = df["Customer Location"].unique()
print("Unique locations:", locations)
locations_values = df["Customer Location"].value_counts()
print("Location values:\n", locations_values)

payment_methods = df["Payment Method"].unique()
print("Unique payment methods:", payment_methods)
payment_methods_values = df["Payment Method"].value_counts()
print("Payment method values:\n", payment_methods_values)

current_status = df["Status"].unique()
print("Unique order statuses:", current_status)
current_status_values = df["Status"].value_counts()
print("Order status values:\n", current_status_values)

total_sales = df["Total Bill"].sum()
print("Total sales amount:", total_sales)

#which product has the highest sales
highest_sales_product = df.groupby("Product")["Total Bill"].sum().idxmax()
highest_sales_value = df.groupby("Product")["Total Bill"].sum().max()
print(f"Product with highest sales: {highest_sales_product} with sales amount of {highest_sales_value}")

# Total sales by product
product_sales= df.groupby("Product")["Total Bill"].sum().sort_values(ascending=False)
print("Product sales:\n", product_sales)


# Visualizations
#1)
plt.figure(figsize=(12, 6))
plt.plot(unique_products, product_vales, marker='o', linestyle='--', color='cyan')
plt.title("Product Sales Distribution",fontdict=font1)
plt.xlabel("Products", fontdict=font)
plt.ylabel("Product Sold", fontdict=font)
plt.grid()
plt.show()

#2)
plt.figure(figsize=(12, 6))
plt.bar(unique_catogories, catogories_values, color='teal',edgecolor='black')
plt.title("Category Sales Distribution",fontdict=font1)
plt.xlabel("Categories", fontdict=font)
plt.ylabel("Total Sold", fontdict=font)
plt.grid(axis='y')
plt.show()

#3)
plt.figure(figsize=(13, 7))
plt.bar(locations, locations_values, color='skyblue', edgecolor='black')
plt.title("Customer Location Distribution",fontdict=font1)
plt.xlabel("Locations", fontdict=font)
plt.ylabel("Total Sold", fontdict=font)
plt.grid(axis='y')
plt.show()

#4)
plt.figure(figsize=(10, 6))
plt.pie(payment_methods_values, labels=payment_methods, autopct='%1.1f%%', startangle=140)
plt.title("Payment Method Distribution", fontdict=font1)
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()

#5)
plt.figure(figsize=(10, 6))
plt.pie(current_status_values, labels=current_status, autopct='%1.1f%%', startangle=140)
plt.title("Order Status Distribution", fontdict=font1)
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()

#6)
plt.figure(figsize=(13, 7))
plt.bar(product_sales.index, product_sales.values, color='orange', edgecolor='black')
plt.title("Total Sales by Product", fontdict=font1)
plt.xlabel("Products", fontdict=font)
plt.ylabel("Total Sales Amount", fontdict=font)
plt.grid()
plt.show()