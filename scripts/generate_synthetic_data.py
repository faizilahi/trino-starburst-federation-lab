import numpy as np, pandas as pd, sqlite3
from pathlib import Path
RNG=np.random.default_rng(5)
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"; DATA.mkdir(parents=True, exist_ok=True)
events=pd.DataFrame({"customer_id":RNG.integers(1,80,400),"event":RNG.choice(["view","cart","purchase"],400),"ts":pd.Timestamp("2024-05-01")})
orders=pd.DataFrame({"order_id":range(1,201),"customer_id":RNG.integers(1,80,200),"amount":RNG.uniform(10,300,200).round(2)})
events.to_csv(DATA/"events.csv",index=False); orders.to_csv(DATA/"orders.csv",index=False)
print("Wrote federation sources")

