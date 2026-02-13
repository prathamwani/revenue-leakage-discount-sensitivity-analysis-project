CREATE DATABASE revenue_leakage;
USE revenue_leakage

CREATE TABLE orders (
    order_id VARCHAR(50),
    order_date DATE,
    category VARCHAR(50),
    sub_category VARCHAR(50),
    region VARCHAR(50),
    sales DECIMAL(10,2),
    discount DECIMAL(4,2),
    profit DECIMAL(10,2),
    quantity INT
);

SELECT 
    category,
    sub_category,
    sales,
    profit,
    discount
FROM orders;

SELECT
    sub_category,
    ROUND(AVG(discount), 2) AS avg_discount,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
WHERE sub_category IN ('Machines', 'Supplies')
GROUP BY sub_category;

SELECT sub_category,
       ROUND(SUM(profit),2) AS total_profit
FROM orders
WHERE sub_category = 'Machines' AND discount < 0.2;

SELECT sub_category,
       ROUND(SUM(profit),2) AS total_profit
FROM orders
WHERE sub_category = 'Machines' AND discount BETWEEN 0.2 AND 0.4;

SELECT sub_category,
       ROUND(SUM(profit),2) AS total_profit
FROM orders
WHERE sub_category = 'Machines' AND discount > 0.4;

SELECT
    category,
    CASE 
        WHEN discount < 0.2 THEN 'Low'
        WHEN discount < 0.4 THEN 'Medium'
        ELSE 'High'
    END AS disc_band,
    ROUND(SUM(profit),2) AS total_profit
FROM orders
GROUP BY category, disc_band;




