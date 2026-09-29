# Trino / Starburst Federation Lab

**Author:** [Faiz Elahi](https://github.com/faizilahi) (`faizilahi`) · **Type:** EDUCATIONAL LAB · **Synthetic data only**

---

## Educational disclaimer

This is an **educational portfolio lab**. Datasets are **synthetic**. It does **not** claim employment at a customer, hospital, bank, SAP shop, or Oracle estate. No real PHI/PII. No live cloud spend. No API keys required.

---

## Problem statement

Analysts need one SQL surface across object storage and RDBMS peers without copying everything into one warehouse first.

**Domain focus:** Multi-source analytics

---

## Why this tool (Apache Trino / Starburst-style federated SQL)

| Heavy ETL copies | Federated SQL across catalogs |
|---|---|
| Silent catalog drift | Explicit connector maps |

---

## Architecture

```mermaid
flowchart LR
  GEN[generate_synthetic_data.py]
  DATA[data/*.csv]
  RUN[run_lab.py]
  OUT[output/*.csv]
  CHART[generate_charts.py]
  IMG[docs/images/*.png]
  GEN --> DATA --> RUN --> OUT
  OUT --> CHART --> IMG
```

See [`docs/architecture.md`](docs/architecture.md).

---

## Dataset dictionary

| Catalog stand-in | Contents |
|------|-------|
| `lake.db` | Parquet-derived events |
| `erp.db` | Orders |
| `output/summary.csv` | Federated join KPI |

---

## Prerequisites

- Python 3.10+
- Packages in `requirements.txt`

---

## How to run

```powershell
cd "trino-/-starburst-federation-lab"
python -m venv .venv
.\\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/run_lab.py
python scripts/generate_charts.py
```

Inspect `output/summary.csv` and `docs/images/primary_metric.png`.

---

## Local vs cloud (honest)

DuckDB attaches multiple local databases as **catalog stand-ins** for Trino catalogs. No Starburst Enterprise cluster.

---

## Results interpretation

Open `output/` CSVs and the PNGs under `docs/images/`. Numbers are synthetic teaching fixtures — use them to explain grain, filters, and control totals, not as real business KPIs.

---

## Limitations

- Stand-in engines (DuckDB/SQLite/pandas) replace paid MPP/warehouses where noted.
- Simplified schemas vs production SAP/Oracle/Hive estates.
- Charts are matplotlib teaching visuals, not vendor BI embeds.

---

## Exercises

1. Add a third catalog for FX rates.
2. Document Ranger-minded access notes.
3. Compare federated vs materialized timings.

---

## License / attribution

Educational portfolio content by Faiz Elahi. Synthetic data for teaching only.

