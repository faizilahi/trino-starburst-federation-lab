def simulate_explain(order_rows: int, customer_rows: int, broadcast_threshold: int = 100000) -> dict:
    broadcast = customer_rows <= broadcast_threshold
    return {
        "fragment_1": f"scan hive.sales.fact_order rows={order_rows}",
        "fragment_2": f"{'broadcast' if broadcast else 'partitioned'} pg.mdm.dim_customer rows={customer_rows}",
        "join": "hash_join remote",
        "broadcast_build": broadcast,
    }
