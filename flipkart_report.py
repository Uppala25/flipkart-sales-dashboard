import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    database="flipkart_project",
    user="postgres",
    password="Ammu@1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# 1️⃣ Total Sales
cur.execute("SELECT SUM(quantity * price_per_unit) FROM sales;")
total_sales = cur.fetchone()[0]
print("Total Sales:", total_sales)

# 2️⃣ Total Profit
cur.execute("""
SELECT SUM((s.price_per_unit - p.cogs) * s.quantity)
FROM sales s
JOIN products p ON s.product_id = p.product_id;
""")
total_profit = cur.fetchone()[0]
print("Total Profit:", total_profit)

# 3️⃣ Top 5 Products
cur.execute("""
SELECT p.product_name, SUM(s.quantity) AS total_sold
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 5;
""")

print("\nTop 5 Products:")
for row in cur.fetchall():
    print(row[0], "-", row[1])

# 4️⃣ Delivery Status
cur.execute("""
SELECT delivery_status, COUNT(*)
FROM shippings
GROUP BY delivery_status;
""")

print("\nDelivery Report:")
for row in cur.fetchall():
    print(row[0], "-", row[1])

cur.close()
conn.close()