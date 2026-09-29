# One Query Across Two Catalogs

[Faiz Elahi](https://www.linkedin.com/in/faizilahi) — [pendataco.com](https://pendataco.com) — [github.com/faizilahi](https://github.com/faizilahi)

Synthetic data only. No vendor-customer employment claim.

Trino/Starburst-style federation joins `hive.sales.fact_order` to
`pg.mdm.dim_customer` in one SQL. The plan note shows a remote hash join with
**50,000** build-side rows broadcast under the size threshold.

## The catalogs

`hive` (DuckDB schema) holds orders; `pg` holds customer master. Wired in
`src/catalogs.py`.

## The join

`sql/federated_revenue.sql` — revenue by customer segment for 2024-03.

## The plan note

Simulated explain: `Fragment 1` scans hive orders (**12,400** rows), `Fragment 2`
broadcasts pg customers (**50,000**). Joined revenue **$6,218,450.00**.

```powershell
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/run_federated.py
```
