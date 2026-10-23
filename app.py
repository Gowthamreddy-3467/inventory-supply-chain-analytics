
import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Inventory & Supply Chain Analytics",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Inventory & Supply Chain Analytics")
st.caption("Live insights from your inventory and supply chain database")


def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        port=int(st.secrets["mysql"]["port"]),
        database=st.secrets["mysql"]["database"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        connection_timeout=10
    )


try:
    with get_connection() as conn:
        kpis = pd.read_sql("""
            SELECT
                COUNT(*) AS total_orders,
                SUM(order_value) AS total_order_value,
                SUM(quantity_ordered) AS quantity_ordered,
                SUM(quantity_received) AS quantity_received
            FROM fact_purchase_orders
        """, conn)

        warehouse_data = pd.read_sql("""
            SELECT
                warehouse_id,
                SUM(order_value) AS total_order_value
            FROM fact_purchase_orders
            GROUP BY warehouse_id
            ORDER BY total_order_value DESC
        """, conn)
        supplier_data = pd.read_sql("""
            SELECT
                s.supplier_id,
                SUM(f.quantity_ordered) AS quantity_ordered,
                SUM(f.quantity_received) AS quantity_received,
                ROUND(
                    100.0 * SUM(f.quantity_received) /
                    NULLIF(SUM(f.quantity_ordered), 0),
                    2
                ) AS fulfillment_rate_pct
            FROM fact_purchase_orders f
            JOIN dim_supplier s
                ON f.supplier_id = s.supplier_id
            GROUP BY s.supplier_id
            ORDER BY fulfillment_rate_pct DESC
            LIMIT 10
        """, conn)

    total_orders = int(kpis.loc[0, "total_orders"] or 0)
    total_value = float(kpis.loc[0, "total_order_value"] or 0)
    ordered = int(kpis.loc[0, "quantity_ordered"] or 0)
    received = int(kpis.loc[0, "quantity_received"] or 0)

    fulfillment_rate = received / ordered * 100 if ordered else 0

    st.subheader("Supply Chain Overview")
 
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Orders", f"{total_orders:,}")
    col2.metric("Total Order Value", f"₹{total_value / 10_000_000:.2f} Cr")
    col3.metric("Quantity Ordered", f"{ordered:,}")
    col4.metric("Fulfillment Rate", f"{fulfillment_rate:.2f}%")

    st.divider()
    st.subheader("Order Value by Warehouse")

    fig = px.bar(
        warehouse_data,
        x="warehouse_id",
        y="total_order_value",
        labels={
            "warehouse_id": "Warehouse",
            "total_order_value": "Total Order Value (₹)"
        },
        text_auto=".3s",
        title="Total Order Value Across Warehouses"
    )

    fig.update_layout(xaxis_title="Warehouse", yaxis_title="Order Value (₹)")
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("Top 10 Suppliers by Fulfillment Rate")

    supplier_fig = px.bar(
        supplier_data,
        x="fulfillment_rate_pct",
        y="supplier_id",
        orientation="h",
        labels={
            "supplier_id": "Supplier ID",
            "fulfillment_rate_pct": "Fulfillment Rate (%)"
        },
        text="fulfillment_rate_pct",
        title="Top 10 Suppliers by Fulfillment Rate"
    )

    supplier_fig.update_layout(
        xaxis_title="Fulfillment Rate (%)",
        yaxis_title="Supplier ID",
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(supplier_fig, use_container_width=True)
    st.success("Successfully connected to MySQL and loaded live data!")

except Exception as e:
    st.error("The application could not load data from MySQL.")
    st.caption(f"Error type: {type(e).__name__}")
    st.caption(str(e))
