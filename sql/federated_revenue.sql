SELECT c.segment,
       ROUND(SUM(o.amount), 2) AS revenue,
       COUNT(*) AS order_count
FROM hive.sales.fact_order o
JOIN pg.mdm.dim_customer c ON c.customer_id = o.customer_id
WHERE o.order_date BETWEEN DATE '2024-03-01' AND DATE '2024-03-31'
GROUP BY 1
ORDER BY revenue DESC
