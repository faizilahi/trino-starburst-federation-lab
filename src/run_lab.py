from pathlib import Path
import duckdb, pandas as pd
ROOT=Path(__file__).resolve().parents[1]
DATA,OUT=ROOT/"data",ROOT/"output"; OUT.mkdir(parents=True, exist_ok=True)
con=duckdb.connect(str(ROOT/"federation.duckdb"))
con.execute(f"CREATE OR REPLACE TABLE lake_events AS SELECT * FROM read_csv_auto('{(DATA/'events.csv').as_posix()}')")
con.execute(f"CREATE OR REPLACE TABLE erp_orders AS SELECT * FROM read_csv_auto('{(DATA/'orders.csv').as_posix()}')")
df=con.execute("""
SELECT e.event, COUNT(DISTINCT e.customer_id) AS customers,
       ROUND(COALESCE(SUM(o.amount),0),2) AS order_amount
FROM lake_events e
LEFT JOIN erp_orders o ON e.customer_id=o.customer_id AND e.event='purchase'
GROUP BY 1 ORDER BY 1
""").df()
df.to_csv(OUT/"summary.csv",index=False); print(df)

