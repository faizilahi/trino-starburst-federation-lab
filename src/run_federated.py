import json, sys
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from catalogs import connect_federated
from plan_note import simulate_explain
DATA, OUT = ROOT / "data", ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    con = connect_federated(DATA)
    sql = (
        "SELECT c.segment, ROUND(SUM(o.amount), 2) AS revenue, COUNT(*) AS order_count "
        "FROM hive_sales.fact_order o "
        "JOIN pg_mdm.dim_customer c ON c.customer_id = o.customer_id "
        "GROUP BY 1 ORDER BY revenue DESC"
    )
    df = con.execute(sql).df()
    total = round(float(df.revenue.sum()), 2)
    plan = simulate_explain(12400, 50000)
    df.to_csv(OUT / "federated_revenue.csv", index=False)
    pd.DataFrame([{"total_revenue": total, **plan}]).to_csv(OUT / "plan_note.csv", index=False)
    print(json.dumps({"total_revenue": total, **plan, "by_segment": df.to_dict("records")}, indent=2))
if __name__ == "__main__":
    main()
