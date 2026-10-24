# 📦 Inventory & Supply Chain Analytics

An end-to-end data analytics project that transforms inventory and supply chain data into actionable business insights using Excel, MySQL, Power BI, and Python Streamlit.

## 🚀 Live Dashboard

**[Launch the Interactive Streamlit App](https://inventory-supply-chain-analytics-3tm5fbibhqzf6bxta62lpn.streamlit.app/)**

## 📊 Project Overview

This project analyzes 18,000 purchase orders to understand supplier performance, warehouse operations, order fulfillment, and delivery delays.

The goal is to help businesses monitor supply chain performance, identify potential inefficiencies, and make data-informed operational decisions.

## 📁 Dataset Overview

- **Purchase orders:** 18,000
- **Suppliers:** 250
- **Warehouses:** 12
- **Date dimension:** 1,096 records

## 🛠️ Tools & Technologies

- **Microsoft Excel:** Data cleaning, data profiling, exploratory data analysis, and PivotTables
- **MySQL:** Relational database design, data storage, joins, and SQL analysis
- **Power BI:** Interactive dashboard and business performance visualizations
- **Python:** Application logic and database connectivity
- **Pandas:** Data processing
- **Plotly:** Interactive charts
- **Streamlit:** Web application and deployment
- **Aiven:** Cloud-hosted MySQL database

## 📈 Key Performance Indicators

- Total purchase orders
- Total order value
- Total quantity ordered and received
- Order fulfillment rate
- Delivery status distribution
- Average delivery delay

## 📊 Dashboard Features

- Supplier performance analysis
- Top 10 suppliers by fulfillment rate
- Order value by warehouse
- Yearly order trends
- Delivery status distribution
- Average delivery delay by warehouse
- Interactive web dashboard

## 🗄️ Database Design

The MySQL database uses a fact-and-dimension structure:

- `fact_purchase_orders` — purchase order metrics and delivery information
- `dim_supplier` — supplier information
- `dim_warehouse` — warehouse information
- `dim_date` — date dimension
- `stg_supply_chain` — original staging table used in the local data workflow

## 🔍 Business Questions Answered

1. What is the overall purchase order fulfillment rate?
2. Which suppliers have the highest fulfillment rates?
3. How does order value vary across warehouses?
4. How have purchase orders changed over time?
5. What is the distribution of delivery statuses?
6. Which warehouses experience higher average delivery delays?

## 💡 Business Value

This project demonstrates how data analytics can support supply chain monitoring by bringing together order, supplier, warehouse, and delivery metrics in a single reporting workflow.

## ▶️ Run the Streamlit App Locally

1. Clone this repository.
2. Install the dependencies:
   `pip install -r requirements.txt`
3. Configure your MySQL connection using Streamlit secrets.
4. Run the application:
   `streamlit run app.py`

Do not upload database passwords or other credentials to GitHub.

## 👨‍💻 Skills Demonstrated

Excel • Data Cleaning • Exploratory Data Analysis • SQL • MySQL • Power BI • Python • Pandas • Plotly • Streamlit • Data Visualization • Business Analytics

## 🔗 Project Links

- **Live application:** [Streamlit Dashboard](https://inventory-supply-chain-analytics-3tm5fbibhqzf6bxta62lpn.streamlit.app/)
- **Source code:** [GitHub Repository](https://github.com/Gowthamreddy-3467/inventory-supply-chain-analytics)

---

*Developed as an end-to-end inventory and supply chain analytics portfolio project.*
