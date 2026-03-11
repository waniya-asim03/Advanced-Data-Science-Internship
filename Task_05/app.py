import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Superstore Dashboard", layout="wide")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("Global_Superstore2.csv")

# Standardize column names: lowercase, strip spaces, replace hyphens with underscores
df.columns = df.columns.str.strip().str.lower().str.replace('-', '_').str.replace(' ', '_')

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filter Options")

# Region filter
if 'region' in df.columns:
    region = st.sidebar.selectbox("Select Region", df['region'].unique())
    df = df[df['region'] == region]

# Category filter
if 'category' in df.columns:
    category = st.sidebar.selectbox("Select Category", df['category'].unique())
    df = df[df['category'] == category]

# Sub-Category filter
if 'sub_category' in df.columns:
    sub_category = st.sidebar.selectbox("Select Sub-Category", df['sub_category'].unique())
    df = df[df['sub_category'] == sub_category]

# -----------------------------
# Metrics
# -----------------------------
st.title("Global Superstore Dashboard")

col1, col2, col3 = st.columns(3)

if 'sales' in df.columns:
    col1.metric("Total Sales", f"${df['sales'].sum():,.2f}")
if 'profit' in df.columns:
    col2.metric("Total Profit", f"${df['profit'].sum():,.2f}")
if 'quantity' in df.columns:
    col3.metric("Total Quantity Sold", f"{df['quantity'].sum():,.0f}")

# -----------------------------
# Top 5 Customers
# -----------------------------
if 'customer_name' in df.columns and 'sales' in df.columns:
    top_customers = df.groupby('customer_name')['sales'].sum().sort_values(ascending=False).head(5)
    st.subheader("Top 5 Customers by Sales")
    st.dataframe(top_customers)

# -----------------------------
# Sales by Sub-Category Chart
# -----------------------------
if 'sub_category' in df.columns and 'sales' in df.columns:
    sales_by_subcat = df.groupby('sub_category')['sales'].sum().sort_values(ascending=False)
    st.subheader("Sales by Sub-Category")
    fig, ax = plt.subplots()
    sns.barplot(x=sales_by_subcat.index, y=sales_by_subcat.values, ax=ax, palette="viridis")
    plt.xticks(rotation=45)
    plt.ylabel("Sales")
    plt.xlabel("Sub-Category")
    st.pyplot(fig)