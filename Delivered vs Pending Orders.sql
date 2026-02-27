SELECT 
delivery_status,
COUNT(*) AS total_orders
FROM shippings
GROUP BY delivery_status;