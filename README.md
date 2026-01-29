# algorithmic-trading-backtest
Distributed trading strategy backtesting with PySpark - 12,300 backtests on 100 stocks
# 📊 Distributed Algorithmic Trading Backtesting Engine

A scalable backtesting framework using PySpark to evaluate trading strategies across 100 stocks.

![Trading Strategy Analysis](bubble_chart.png)

## 🎯 Project Overview

Built a distributed backtesting engine that processes **12,300 backtests** across **100 stocks**, analyzing **303,600 price records** spanning 10 years of real market data (2014-2026).

### Key Results
- **12,300** backtests completed
- **123** trading strategies tested (MA, RSI, MACD, Mean Reversion)
- **100** stocks analyzed (S&P 500 constituents)
- **303,600** price records processed
- **Best Strategy:** RSI with 0.27 Sharpe ratio, 38.5% returns
- **Platform:** Kaggle (30GB RAM, FREE)

## 📈 Performance Highlights

**Top 5 Strategies:**
1. **RSI (14, 30, 70)** - Sharpe: 0.274, Return: 38.5%
2. **RSI (21, 25, 75)** - Sharpe: 0.218, Return: 31.0%
3. **RSI (14, 25, 75)** - Sharpe: 0.216, Return: 13.7%
4. **RSI (21, 30, 70)** - Sharpe: 0.213, Return: 16.7%
5. **RSI (28, 30, 70)** - Sharpe: 0.199, Return: 37.1%

**Key Finding:** RSI mean-reversion strategies outperformed trend-following approaches during the volatile 2014-2026 period, demonstrating robust performance across multiple market cycles.

## 🛠️ Tech Stack

- **Big Data:** PySpark 3.5
- **Data Processing:** pandas, NumPy
- **Data Source:** yfinance (Yahoo Finance API)
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Platform:** Kaggle Notebooks (30GB RAM)
- **Languages:** Python 3.12

## 🚀 Quick Start

### Run on Kaggle (Recommended)
1. Open [Kaggle_Trading_Backtest.ipynb](Kaggle_Trading_Backtest.ipynb) on Kaggle
2. Enable Internet in Settings
3. Run all cells (takes ~30-60 minutes)

### Run Locally
```bash
pip install -r requirements.txt
jupyter notebook
# Open and run the notebook
```

## 📊 Visualizations

### Complete Analysis Dashboard
![Dashboard](dashboard.png)

*9-panel interactive dashboard showing comprehensive strategy performance analysis*

### Risk-Return Analysis
See bubble chart above - interactive version available in notebook with hover details.

## 🎓 What I Learned

- **Distributed Computing:** PySpark architecture, pandas UDFs, data partitioning
- **Quantitative Finance:** Sharpe ratio, Calmar ratio, max drawdown, win rate
- **Big Data Processing:** Handling 300K+ records efficiently
- **Strategy Validation:** Testing across market cycles (COVID crash, bull/bear markets)
- **Data Visualization:** Professional dashboards with Plotly

## 💡 Key Insights

1. **RSI strategies dominated** - Mean-reversion outperformed during choppy markets
2. **Market cycles matter** - Same strategy performs differently in bull vs bear markets
3. **Validation is crucial** - Testing across 100 stocks prevents overfitting
4. **Distributed processing** - PySpark enables analysis that would take hours sequentially

## 🔮 Future Enhancements

- [ ] Deploy to AWS EMR for 500+ stock scale
- [ ] Add walk-forward analysis
- [ ] Implement transaction costs
- [ ] Real-time backtesting with streaming data
- [ ] ML-based parameter optimization

## 📝 Technical Details

**Backtesting Engine:**
- Parallel execution across Spark workers
- Vectorized calculations with pandas UDFs
- Smart data partitioning by ticker
- Comprehensive performance metrics

**Strategies Tested:**
- Moving Average (32 variations)
- RSI (45 variations)
- MACD (27 variations)
- Mean Reversion / Bollinger Bands (20 variations)

## 📫 Contact

[Your Name] - [Your Email] - [LinkedIn Profile]

Project built: January 2026

---

**⭐ Star this repo if you find it useful!**
