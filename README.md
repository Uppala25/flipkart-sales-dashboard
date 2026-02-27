# 📊 Flipkart Sales Dashboard (PostgreSQL + Streamlit)

## 🚀 Project Overview

This project analyzes Flipkart sales data using PostgreSQL and Python.
It provides actionable business insights including revenue trends, profit margins,
category performance, state-wise sales distribution, and delivery status analysis.

The dashboard is built using Streamlit and integrates directly with a PostgreSQL database.

---

## 🛠 Tech Stack

- PostgreSQL
- Python
- Pandas
- Streamlit
- Matplotlib
- SQL (Joins, Aggregations, Group By, Date Functions)
- Git & GitHub

---

## 📊 Key Features

- ✔ Total Sales KPI
- ✔ Total Profit Calculation
- ✔ Monthly Sales Trend Analysis
- ✔ State-wise Sales Breakdown
- ✔ Category-wise Profit Analysis
- ✔ Delivery Status Distribution
- ✔ SQL Joins Across Multiple Tables

---

## 🗄 Database Schema

The project uses the following tables:

- customers
- products
- sales
- payments
- shippings

Relationships:
- sales links customers and products
- payments and shippings are connected via order_id
- profit is calculated using product COGS and selling price

## ▶ How to Run the Project Locally
1. Clone the repository
2. Install requirements
3. Run:
   streamlit run flipkart_dashboard.py

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/flipkart-sales-dashboard.git
