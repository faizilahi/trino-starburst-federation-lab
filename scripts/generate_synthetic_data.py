from pathlib import Path
import numpy as np, pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"; DATA.mkdir(parents=True, exist_ok=True)
RNG = np.random.default_rng(6218)
cust = pd.DataFrame({
    "customer_id": [f"C{i:05d}" for i in range(50000)],
    "segment": RNG.choice(["SMB", "Mid", "Enterprise"], 50000, p=[0.5, 0.35, 0.15]),
})
orders = pd.DataFrame({
    "order_id": [f"O{i:05d}" for i in range(12400)],
    "customer_id": [f"C{int(RNG.integers(0,50000)):05d}" for _ in range(12400)],
    "order_date": RNG.choice(pd.date_range("2024-03-01", "2024-03-31").astype(str), 12400),
    "amount": RNG.uniform(50, 1200, 12400).round(2),
})
factor = 6218450 / orders.amount.sum()
orders["amount"] = (orders["amount"] * factor).round(2)
orders.iloc[-1, orders.columns.get_loc("amount")] += round(6218450 - orders.amount.sum(), 2)
cust.to_csv(DATA / "dim_customer.csv", index=False)
orders.to_csv(DATA / "fact_order.csv", index=False)
print("orders", len(orders), "customers", len(cust), "rev", orders.amount.sum())
