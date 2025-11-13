import streamlit as st
import numpy as np
import pandas as pd

# -----------------------
# Step 1: Generate Sample Sales Data
# -----------------------

# Simulate data for 12 months, 6 products
months = 12
products = 6

np.random.seed(42)  # reproducible results

# Random units sold for each product per month (range 50 to 300)
units_sold = np.random.randint(50, 301, size=(months, products))

# Random unit price for each product (range Rs. 100 to Rs. 1000)
unit_price = np.random.randint(100, 1001, size=products)

# Random cost price for profit calculation (80% of selling price approx)
cost_price = (unit_price * np.random.uniform(0.6, 0.8, size=products)).astype(int)

# Product names
product_names = np.array(['Shirt', 'Trousers', 'Shoes', 'Bags', 'Jackets', 'Watches'])

# -----------------------
# Step 2: Revenue and Profit Calculation
# -----------------------

# Calculate revenue per month per product
revenue = units_sold * unit_price

# Total revenue per product (over 12 months)
total_revenue_per_product = revenue.sum(axis=0)

# Total revenue per month
total_revenue_per_month = revenue.sum(axis=1)

# Calculate cost
cost = units_sold * cost_price

# Profit = Revenue - Cost
profit = revenue - cost
total_profit_per_product = profit.sum(axis=0)
total_profit = profit.sum()

# -----------------------
# Step 3: Analysis
# -----------------------

# Most profitable product
max_profit_index = np.argmax(total_profit_per_product)

# Best-selling product (based on total units)
total_units_per_product = units_sold.sum(axis=0)
top_selling_index = np.argmax(total_units_per_product)

# Month with highest revenue
best_month = np.argmax(total_revenue_per_month)

# -----------------------
# Step 4: Filtering and Reporting
# -----------------------

# Find products with profit > ₹150000
high_profit_mask = total_profit_per_product > 150000
high_profit_products = product_names[high_profit_mask]

# Reshape revenue data for better view (6 rows, 12 columns)
revenue_reshaped = revenue.T

# Average revenue per product per month
avg_revenue = np.mean(revenue, axis=0)

# -----------------------
# Step 5: Summary Report
# -----------------------

# Prepare DataFrames
df_products = pd.DataFrame({
    "Product": product_names,
    "Unit Price": unit_price,
    "Cost Price": cost_price,
    "Total Revenue": total_revenue_per_product,
    "Total Profit": total_profit_per_product,
    "Units Sold": total_units_per_product,
    "Avg Monthly Revenue": avg_revenue.astype(int)
})

df_monthly = pd.DataFrame({
    "Month": [f"Month {i+1}" for i in range(months)],
    "Total Revenue": total_revenue_per_month
})

st.set_page_config(page_title="Sales Data Dashboard", layout="wide")

st.sidebar.title("📊 Navigation")
section = st.sidebar.radio("Go to", ["Overview", "Product Analysis", "Monthly Trends", "Business Summary"])

st.title("🛍️ Sales Data Dashboard")

if section == "Overview":
    st.header("Product Overview")
    st.dataframe(df_products, use_container_width=True)
    st.info(f"High Profit Products (> ₹150000): {', '.join(high_profit_products)}")
    st.metric("Total Revenue (Year)", f"₹{revenue.sum():,}")
    st.metric("Total Profit (Year)", f"₹{total_profit:,}")

elif section == "Product Analysis":
    st.header("Total Revenue per Product")
    st.bar_chart(df_products.set_index("Product")["Total Revenue"])
    st.header("Total Profit per Product")
    st.bar_chart(df_products.set_index("Product")["Total Profit"])
    st.header("Units Sold per Product")
    st.bar_chart(df_products.set_index("Product")["Units Sold"])
    st.header("Average Monthly Revenue per Product")
    st.bar_chart(df_products.set_index("Product")["Avg Monthly Revenue"])

elif section == "Monthly Trends":
    st.header("Monthly Revenue Trend")
    st.line_chart(df_monthly.set_index("Month"))
    best_month = np.argmax(total_revenue_per_month)
    st.success(f"📈 Highest Revenue Month: Month {best_month+1} (₹{total_revenue_per_month[best_month]:,})")

elif section == "Business Summary":
    st.header("Business Summary")
    st.markdown(f"""
    - **Total Revenue (Year):** ₹{revenue.sum():,}
    - **Total Profit (Year):** ₹{total_profit:,}
    - **Avg Revenue/Month:** ₹{int(np.mean(total_revenue_per_month)):,}
    - **Top Selling Product:** {product_names[np.argmax(total_units_per_product)]} ({total_units_per_product[np.argmax(total_units_per_product)]} units)
    - **Least Selling Product:** {product_names[np.argmin(total_units_per_product)]}
    - **Total Units Sold:** {units_sold.sum():,}
    """)


# for run first
# cd "c:\Users\good day\Desktop\Python\real life projects"
# after that run
#streamlit run sales_data_analysis.py
