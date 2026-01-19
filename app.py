import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from prophet import Prophet

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Supply Chain Optimization Dashboard",
    layout="wide"
)

st.title("📦 Supply Chain Optimization Dashboard")

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

@st.cache_data
def load_data():
    conn = sqlite3.connect("supply_chain_db.db")
    df = pd.read_sql("SELECT * FROM sales", conn)
    return df

sales_df = load_data()

# -----------------------------
# DATA PREVIEW
# -----------------------------

st.subheader("🔍 Sales Data Preview")
st.dataframe(sales_df.head(20))

# -----------------------------
# DATE CLEANING
# -----------------------------

sales_df['Order_Date'] = pd.to_datetime(
    sales_df['Order_Date'],
    dayfirst=True,
    errors='coerce'
)

# -----------------------------
# KPI METRICS
# -----------------------------

st.subheader("📊 Business Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Orders", len(sales_df))

with col2:
    st.metric("Total Quantity Sold", int(sales_df['Quantity'].sum()))

with col3:
    st.metric("Total Revenue", round(sales_df['Sales'].sum(), 2))

with col4:
    st.metric("Unique Products", sales_df['Product Name'].nunique())

# -----------------------------
# DEMAND TREND CHART
# -----------------------------

st.subheader("📈 Daily Demand Trend")

daily_sales = sales_df.groupby(
    'Order_Date',
    as_index=False
)['Quantity'].sum()

st.line_chart(
    daily_sales.set_index('Order_Date')['Quantity']
)

# -----------------------------
# FORECAST SECTION
# -----------------------------

st.subheader("🔮 Demand Forecast (Next 30 Days)")

# Select product
product_list = sales_df['Product Name'].unique()
selected_product = st.selectbox(
    "Select Product for Forecast",
    product_list
)

product_data = sales_df[sales_df['Product Name'] == selected_product]

forecast_data = product_data[['Order_Date', 'Quantity']]
forecast_data.columns = ['ds', 'y']

# Train model only if enough data
if len(forecast_data) > 10:

    model = Prophet()
    model.fit(forecast_data)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    forecast_chart = forecast[['ds', 'yhat']].set_index('ds')

    st.line_chart(forecast_chart)

else:
    st.warning("Not enough data for forecasting this product.")

# -----------------------------
# INVENTORY OPTIMIZATION LOGIC
# -----------------------------

st.subheader("📦 Inventory Reorder Decision System")

# Demand calculation
avg_demand = sales_df.groupby(
    'Product Name',
    as_index=False
)['Quantity'].mean()

# Business constants
LEAD_TIME = 7
ORDERING_COST = 50
HOLDING_COST = 2

# Inventory formulas
avg_demand['Reorder_Point'] = avg_demand['Quantity'] * LEAD_TIME
avg_demand['Annual_Demand'] = avg_demand['Quantity'] * 365

avg_demand['EOQ'] = np.sqrt(
    (2 * avg_demand['Annual_Demand'] * ORDERING_COST) / HOLDING_COST
)

# Simulate stock
np.random.seed(42)
avg_demand['Current_Stock'] = np.random.randint(10, 150, size=len(avg_demand))

# Decision rule
avg_demand['Decision'] = np.where(
    avg_demand['Current_Stock'] <= avg_demand['Reorder_Point'],
    "REORDER",
    "NO ACTION"
)

# Final decision table
decision_table = avg_demand[[
    'Product Name',
    'Current_Stock',
    'Reorder_Point',
    'EOQ',
    'Decision'
]]

st.dataframe(decision_table)

# -----------------------------
# ALERT SUMMARY
# -----------------------------

st.subheader("🚨 Reorder Alert Summary")

reorder_count = (decision_table['Decision'] == 'REORDER').sum()

st.metric("Products Needing Reorder", reorder_count)

# -----------------------------
# FOOTER
# -----------------------------

st.success("✅ Supply Chain Optimization Dashboard Loaded Successfully")
