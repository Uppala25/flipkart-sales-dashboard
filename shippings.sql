CREATE TABLE shippings (
    shipping_id INT PRIMARY KEY,
    order_id INT,
    shipping_date DATE,
    return_date DATE,
    shipping_providers VARCHAR(55),
    delivery_status VARCHAR(55)
);