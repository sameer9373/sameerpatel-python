# superstore_streamlit.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset (Simple way)
# -------------------------------
st.title("📊 Superstore Sales Dashboard")
st.markdown("This is an **interactive data analysis app** built with Streamlit using Superstore dataset.")

# Change path to where your CSV is stored
df = pd.read_csv("C:/Users/good day/Desktop/Python/real life projects/superstore_subset.csv", parse_dates=["Order Date", "Ship Date"])

# -------------------------------
# 2. Sidebar Filters
# -------------------------------
st.sidebar.header("🔍 Filter Data")

region = st.sidebar.multiselect("Select Region:", df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Select Category:", df["Category"].unique(), default=df["Category"].unique())

# Apply Filters
filtered_df = df[(df["Region"].isin(region)) & (df["Category"].isin(category))]

st.write("### 📂 Data Preview", filtered_df.head())

# -------------------------------
# 3. KPI Metrics
# -------------------------------
st.subheader("📌 Key Metrics")
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
avg_discount = filtered_df["Discount"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Avg. Discount", f"{avg_discount:.2%}")

# -------------------------------
# 4. Charts & Visualizations
# -------------------------------

st.subheader("📈 Sales Trend Over Time")
sales_trend = filtered_df.groupby("Order Date")["Sales"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(sales_trend["Order Date"], sales_trend["Sales"], color="blue")
ax.set_title("Daily Sales Trend")
st.pyplot(fig)

st.subheader("📊 Sales by Category")
cat_sales = filtered_df.groupby("Category")["Sales"].sum().sort_values()
fig, ax = plt.subplots()
cat_sales.plot(kind="bar", color="orange", ax=ax)
ax.set_ylabel("Sales")
st.pyplot(fig)

st.subheader("🥧 Profit by Region")
region_profit = filtered_df.groupby("Region")["Profit"].sum()
fig, ax = plt.subplots()
ax.pie(region_profit, labels=region_profit.index, autopct="%1.1f%%", startangle=90)
st.pyplot(fig)

st.subheader("📉 Discount vs Profit")
fig, ax = plt.subplots()
sns.scatterplot(x="Discount", y="Profit", data=filtered_df, ax=ax, color="red")
st.pyplot(fig)

st.subheader("🔥 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(filtered_df[["Sales", "Profit", "Discount", "Quantity"]].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# -------------------------------
# 5. Insights / Report
# -------------------------------
st.subheader("📢 Executive Insights")
st.markdown("""
- **Technology** category is usually the highest revenue driver.
- **Furniture** often struggles with profitability despite good sales.
- High **Discounts** tend to reduce overall profit margins.
- The **West region** usually contributes the highest revenue in this dataset.
""")
