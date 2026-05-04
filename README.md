# Distributed Algorithmic Trading Backtesting Engine

A production-grade backtesting framework using PySpark to evaluate **123 trading strategies** across **100 S&P 500 stocks** over 10 years of real market data, with an interactive Streamlit dashboard for exploring results.

![3D Strategy Analysis](3D%20visualization.png)

---

## Results at a Glance

| Metric | Value |
|---|---|
| Total backtests | 12,300 |
| Strategies tested | 123 (MA, RSI, MACD, Mean Reversion) |
| Stocks analyzed | 100 S&P 500 constituents |
| Price records processed | 303,600 |
| Time period | 10 years (2014–2026) |
| Best Sharpe ratio | **0.274** (RSI strategy) |
| Best total return | **38.5%** |
| Throughput | **240 backtests / second** |
| Data quality score | **100%** (5/5 validation checks) |

**Key finding:** RSI mean-reversion strategies dominated the top 5, outperforming trend-following approaches across the 2014–2026 period (COVID crash, 2022 bear market, AI bull run).

---

## Top 5 Strategies

| Rank | Type | Sharpe | Return | Drawdown | Win Rate |
|------|------|--------|--------|----------|----------|
| 1 | RSI | 0.274 | 38.5% | −32.2% | 7.7% |
| 2 | RSI | 0.218 | 31.0% | −36.2% | 10.0% |
| 3 | Mean Reversion | 0.216 | 13.7% | −20.3% | 1.9% |
| 4 | RSI | 0.213 | 16.7% | −26.7% | 3.8% |
| 5 | RSI | 0.199 | 37.1% | −39.6% | 13.0% |

---

## Interactive Dashboard

Results are explored through a **4-page Streamlit dashboard** — replacing the static screenshots with interactive Plotly charts.

![Complete Dashboard](Complete%20Trading%20Backtesting%20analysis%20dashboard.png)

| Page | What it shows |
|---|---|
| **Overview** | KPI cards, strategy counts by type, per-type summary table |
| **Strategy Explorer** | Rotatable 3D scatter (Return × Drawdown × Sharpe) with sidebar filters; filterable top-N table |
| **Type Comparison** | Radar chart across 4 strategy types; grouped bar + box-plot distributions |
| **Monitoring** | Data quality gauge (100%), throughput indicator, 5 validation checks |

![Monitoring Dashboard](Production%20Monitoring%20Dashboard.png)

### Running the dashboard

```bash
# 1. Run the notebook to generate results
#    Open algorithmic-backtesting.ipynb and run all cells,
#    including the export cell at the bottom.

# 2. Install dashboard dependencies (no PySpark needed)
pip install -r requirements_dashboard.txt

# 3. Launch
streamlit run app.py
```

---

## Visualizations

### Strategy Type Performance
![Strategy Type Comparison](Strategy%20Type%20Performance%20Comparison.png)

### Top 15 Strategies
![Top 15 Strategies](Top%2015%20trading%20strategies.png)

---

## How It Works

### Data Pipeline
```
Yahoo Finance (yfinance)
    ↓
5-step Data Validation
    ↓
PySpark Distributed DataFrame
    ↓
Strategy Grid (123 parameter combinations)
    ↓
Parallel Backtesting via pandas UDFs
    ↓
Performance Aggregation
    ↓
results.csv  →  Streamlit Dashboard
```

### Strategies Tested

| Type | Combinations | Parameters |
|---|---|---|
| Moving Average | 12 | Short window: 20/50/100/200; Long window: 50–200 |
| RSI | 45 | Period: 7/9/14/21/28; Oversold: 20/25/30; Overbought: 70/75/80 |
| MACD | 27 | Fast: 8/12/16; Slow: 20/26/32; Signal: 7/9/11 |
| Mean Reversion | 20 | Window: 10–30; Std dev multiplier: 1.5/2.0/2.5/3.0 |

### Metrics Calculated per Strategy
- **Sharpe ratio** — annualized (√252 × mean/std)
- **Maximum drawdown** — peak-to-trough decline
- **Total return** — cumulative over 10 years
- **Calmar ratio** — annual return / |max drawdown|
- **Win rate** — proportion of positive-return days

### Data Quality Monitoring
All 5 checks pass at 100%:
- **Completeness** — null value detection
- **Price validity** — OHLC relationship checks
- **Data freshness** — staleness detection
- **Coverage** — stock consistency across time
- **OHLC logic** — High ≥ Open/Close/Low, Low ≤ Open/Close/High

---

## Quick Start

### Kaggle (recommended — 30 GB RAM, free)
1. Open [`algorithmic-backtesting.ipynb`](algorithmic-backtesting.ipynb) on Kaggle
2. Enable **Internet** in notebook settings
3. Run all cells (~30–60 min)
4. Run the final export cell to generate `data/results.csv`

### Google Colab (12 GB RAM)
1. Open [`colab_quick_demo.ipynb`](colab_quick_demo.ipynb)
2. Run all cells (~15–30 min)
3. Scaled-down demo: 30 stocks, 3,690 backtests

### Local
```bash
git clone https://github.com/Het415/algorithmic-trading-backtest.git
cd algorithmic-trading-backtest

# Full backtesting engine (requires PySpark)
pip install -r requirements.txt
jupyter notebook algorithmic-backtesting.ipynb

# Dashboard only (no PySpark)
pip install -r requirements_dashboard.txt
streamlit run app.py
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Distributed computing | PySpark 3.5, pandas UDFs |
| Data | yfinance, PyArrow / Parquet |
| Numerics | pandas, NumPy, SciPy |
| Visualization | Plotly, Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Platform | Kaggle (30 GB RAM) / AWS EMR |

---

## Project Structure

```
algorithmic-trading-backtest/
├── algorithmic-backtesting.ipynb     # Main notebook — 100 stocks, full scale
├── colab_quick_demo.ipynb            # Quick demo — 30 stocks
├── app.py                            # Streamlit dashboard entrypoint
├── requirements.txt                  # Full dependencies (includes PySpark)
├── requirements_dashboard.txt        # Dashboard-only dependencies
├── dashboard/
│   ├── components/charts.py          # Plotly figure factories
│   ├── data/loader.py                # Cached CSV + metadata loader
│   └── pages/
│       ├── overview.py
│       ├── strategy_explorer.py
│       ├── type_comparison.py
│       └── monitoring.py
└── data/
    ├── results.csv                   # Generated by notebook (gitignored)
    └── metadata.json                 # Run metadata (gitignored)
```

---

## Future Work

- [ ] Walk-forward analysis for out-of-sample robustness
- [ ] Transaction costs and slippage modeling
- [ ] AWS EMR deployment for 500+ stock scale
- [ ] Real-time backtesting with streaming data (Kafka)
- [ ] Bayesian parameter optimization
- [ ] Multi-strategy portfolio optimization

---

## Contact

**Het Prajapati** — [LinkedIn](https://www.linkedin.com/in/het-prajapati6210/) · hetprajapati6210@gmail.com

---

⭐ Star this repo if you found it useful!
