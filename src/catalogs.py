import duckdb
from pathlib import Path

def connect_federated(data: Path):
    con = duckdb.connect()
    con.execute("CREATE SCHEMA hive_sales")
    con.execute("CREATE SCHEMA pg_mdm")
    con.execute(f"CREATE TABLE hive_sales.fact_order AS SELECT * FROM read_csv_auto('{(data/'fact_order.csv').as_posix()}')")
    con.execute(f"CREATE TABLE pg_mdm.dim_customer AS SELECT * FROM read_csv_auto('{(data/'dim_customer.csv').as_posix()}')")
    return con
