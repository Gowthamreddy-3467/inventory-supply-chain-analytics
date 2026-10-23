# Inventory & Supply Chain Analytics Dashboard

## Project Overview
An interactive analytics dashboard that provides insights into inventory and supply chain operations using data stored in MySQL.

## Key Features
- KPI cards for total orders, total order value, quantity ordered, and fulfillment rate.
- Interactive chart showing order value by warehouse.
- Top 10 suppliers ranked by fulfillment rate.
- Live data retrieval from a MySQL database.
- Interactive visualizations built with Plotly and Streamlit.

## Technology Stack
- Python
- Streamlit
- Pandas
- Plotly
- MySQL

## Database
Database name: `inventory_supply_chain`

The database includes supplier, warehouse, date, and purchase order tables.

## Run Locally

1. Install Python.
2. Install the required libraries:

   `pip install -r requirements.txt`

3. Configure your MySQL credentials in `.streamlit/secrets.toml`.
4. Ensure MySQL is running and the database has been created.
5. Start the dashboard:

   `python -m streamlit run app.py`

## Security
Database credentials are stored locally in `.streamlit/secrets.toml`. Do not publish passwords or other sensitive credentials to GitHub.

## Project Status
The dashboard currently displays supply chain KPIs and visualizations using live MySQL data.


## Analytics Dashboards

### 1. Excel Dashboard
The Excel component covers data cleaning, exploratory analysis, and dashboard reporting.

**File:** `inventory-supply-chain-v1.0.0-analysis(1).xlsx`

### 2. Power BI Dashboard
The Power BI component presents supply chain KPIs and interactive visualizations.

**File:** `Inventory_Supply_Chain_Dashboard.pbix`

### 3. Python Streamlit Dashboard
The Streamlit application connects to MySQL and displays live supply chain KPIs and charts.

**File:** `app.py`

## Skills Demonstrated
- Excel data cleaning and exploratory analysis
- SQL and MySQL database querying
- Power BI dashboard development
- Python, Pandas, and Plotly
- Streamlit application development
- Supply chain KPI analysis
