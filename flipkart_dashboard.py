import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# SIMPLE LOGIN SYSTEM
# -------------------------
def login():
    st.title("🔐 Flipkart Analytics Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Wrong Credentials")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# -------------------------
# DATABASE CONNECTION
# -------------------------
conn = psycopg2.connect(
    database="flipkart_project",
    user="postgres",
    password="Ammu@1234",
    host="localhost",
    port="5432"
)

st.title("📊 Flipkart  Dashboard")

# -------------------------
# FILTERS
# -------------------------
state_query = "SELECT DISTINCT state FROM customers;"
category_query = "SELECT DISTINCT category FROM products;"

states = pd.read_sql(state_query, conn)['state'].tolist()
categories = pd.read_sql(category_query, conn)['category'].tolist()

selected_state = st.selectbox("Select State", ["All"] + states)
selected_category = st.selectbox("Select Category", ["All"] + categories)

# -------------------------
# BUILD WHERE CONDITIONS
# -------------------------
where_conditions = []

if selected_state != "All":
    where_conditions.append(f"c.state = '{selected_state}'")

if selected_category != "All":
    where_conditions.append(f"p.category = '{selected_category}'")

where_clause = ""
if where_conditions:
    where_clause = "WHERE " + " AND ".join(where_conditions)

# -------------------------
# MAIN QUERY
# -------------------------
main_query = f"""
SELECT 
c.state,
p.category,
s.quantity,
s.price_per_unit,
(p.cogs)
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
{where_clause};
"""

df = pd.read_sql(main_query, conn)

# -------------------------
# KPIs
# -------------------------
total_sales = (df['quantity'] * df['price_per_unit']).sum()
total_profit = ((df['price_per_unit'] - df['cogs']) * df['quantity']).sum()
total_orders = len(df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹ {round(total_sales,2)}")
col2.metric("Total Profit", f"₹ {round(total_profit,2)}")
col3.metric("Total Orders", total_orders)

# -------------------------
# CATEGORY SALES GRAPH
# -------------------------
st.subheader("Category Sales")

category_sales = df.groupby("category").apply(
    lambda x: (x['quantity'] * x['price_per_unit']).sum()
)

plt.figure()
plt.bar(category_sales.index, category_sales.values)
plt.xticks(rotation=45)
plt.title("Category Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

st.pyplot(plt)

# -------------------------
# STATE SALES GRAPH
# -------------------------
st.subheader("State Sales")

state_sales = df.groupby("state").apply(
    lambda x: (x['quantity'] * x['price_per_unit']).sum()
)

plt.figure()
plt.bar(state_sales.index, state_sales.values)
plt.xticks(rotation=45)
plt.title("State Sales")
plt.xlabel("State")
plt.ylabel("Sales")

st.pyplot(plt)

# -------------------------
# DOWNLOAD CSV
# -------------------------
st.subheader("Download Filtered Report")

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_flipkart_report.csv",
    mime="text/csv"
)

conn.close()
