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
