SELECT 
SUM((s.price_per_unit - p.cogs) * s.quantity) AS total_profit
FROM sales s
JOIN products p ON s.product_id = p.product_id;