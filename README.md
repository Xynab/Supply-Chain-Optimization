📦 **Supply Chain Optimization & Demand Forecasting Dashboard**

📌 **Overview**<img width="1366" height="768" alt="Screenshot 2026-01-19 005928" src="https://github.com/user-attachments/assets/b3dc7fae-c419-4331-99ff-05d8f1fc83e9" />
<img width="1366" height="768" alt="forecast_view png" src="https://github.com/user-attachments/assets/eac638b9-7bea-424a-add6-a981e6478efa" />
<img width="1366" height="768" alt="dashboard_home png" src="https://github.com/user-attachments/assets/a0a823f1-8f04-457a-a0d0-6f20bbade4f2" />


This project implements an end-to-end Supply Chain Optimization System that analyzes sales data, forecasts future demand, and optimizes inventory decisions using data-driven business logic and interactive dashboards.

The project was built from scratch — covering data processing, forecasting, optimization modeling, and visualization — to simulate how real-world inventory planning systems work.

🎯 **Why This Project**

Inventory management is one of the biggest challenges in supply chain operations. Poor demand planning can lead to stockouts, overstocking, and revenue loss.

This project answers key business questions:

How can historical sales data be used to forecast future demand?

How can reorder decisions be automated using optimization models?

How can dashboards support real-time inventory monitoring?

🏢 **Use Cases**

Inventory planning & replenishment

Demand forecasting

Warehouse stock monitoring

Supply chain analytics dashboards

Retail operations optimization

📊 **Dataset Details**

Source: Kaggle – Sales Forecasting Dataset
Domain: Retail Sales
Time Period: Historical transaction data
Granularity: Order-level data
Region: Multi-region retail data

🧠 What I Built (Simple Explanation)
1️⃣ **Data Collection & Storage**

Loaded structured sales data into SQL database

Designed a clean data pipeline for analytics

2️⃣ **Data Cleaning & Processing**

Handled missing values

Standardized date formats

Prepared aggregated daily demand metrics

3️⃣ **Demand Analysis**

Created daily and rolling demand trends

Analyzed sales patterns across time

4️⃣ **Demand Forecasting**

Implemented time-series forecasting using Prophet

Generated 30-day future demand predictions

Visualized forecast uncertainty ranges

5️⃣ **Inventory Optimization Logic**

Implemented core inventory planning models:

Reorder Point (ROP) calculation

Economic Order Quantity (EOQ) optimization

Safety stock estimation

Automated reorder decision rules

6️⃣ **Interactive Dashboard**

Built a professional Streamlit dashboard that includes:

Sales and demand trend visualization

Forecast charts

Inventory decision tables

KPI summary metrics

Reorder alert indicators

📊 **Key Insights**

Demand patterns show strong seasonal and temporal trends

Forecasting improves planning accuracy compared to static averages

EOQ-based ordering reduces excess inventory risk

Automated alerts improve response time for replenishment decisions

💼 **Business Value**

Reduces stockout and overstock risks

Supports data-driven inventory decisions

Improves operational planning efficiency

Demonstrates scalable analytics architecture

⚠️**Limitations**

Uses historical batch data (not real-time)

External factors like promotions are not included

Forecast accuracy depends on data quality

🚀 **Future Improvements**

Real-time sales data streaming

Multi-warehouse inventory optimization

Advanced forecasting models (LSTM, XGBoost)

Supplier lead-time modeling

Cloud deployment of dashboard

🛠 **Tech Stack**

Python

SQL (SQLite)

Pandas, NumPy

Prophet (Time-Series Forecasting)

Streamlit (Dashboard & Visualization)

▶️ **How To Run**

pip install -r requirements.txt
streamlit run app.py

✨ **Final Note**

This project reflects my approach to solving real-world data problems by combining analytics, forecasting, optimization, and visualization into a complete decision-support system.

⭐ If you find this project useful, feel free to give it a star!
