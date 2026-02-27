CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
	order_status VARCHAR(25),
    product_id INT,
    quantity INT,
    price_per_unit DOUBLE PRECISION
);