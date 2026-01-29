# 📊 Distributed Algorithmic Trading Backtesting Engine

A production-grade backtesting framework using PySpark to evaluate trading strategies across 100 stocks with comprehensive monitoring and quality assurance.

![Trading Strategy Analysis](3D%20visualization.png)

## 🎯 Project Overview

Built a **distributed backtesting engine** that processes **12,300 backtests** across **100 stocks**, analyzing **303,600 price records** spanning 10 years of real market data (2014-2026) with production-grade monitoring and data quality validation.

### Key Results
- 📊 **12,300** backtests completed
- 🧪 **123** trading strategies tested (MA, RSI, MACD, Mean Reversion)
- 💹 **100** stocks analyzed (S&P 500 constituents)
- 📈 **303,600** price records processed
- 🏆 **Best Sharpe:** 0.274 (RSI strategy)
- 🎯 **Best Return:** 38.5%
- ⚡ **Throughput:** 240 backtests/second
- 💻 **Platform:** Kaggle (30GB RAM, FREE)
- ✅ **Data Quality:** 100% validation pass rate

## 📈 Visualizations

### Complete Analysis Dashboard
![Dashboard](Top%2015%20trading%20strategies.png)

*Comprehensive 9-panel dashboard showing strategy performance, distributions, and risk-return profiles*

### Production Monitoring Dashboard
![Monitoring](Production%20Monitoring%20Dashboard.png)

*Real-time monitoring showing data quality score (100%), throughput (240 tests/sec), and automated validation checks*

### Strategy Type Comparison
![Strategy Types](Strategy%20Type%20Performance%20Comparison.png)

*Performance comparison across different strategy categories*

### Top Strategies
![Top 15](Top%2015%20trading%20strategies.png)

*Interactive table showing top 15 performing strategies with complete metrics*

## 🏆 Top 5 Strategies

| Rank | Type | Sharpe | Return | Drawdown | Win Rate | Stocks Tested |
|------|------|--------|--------|----------|----------|---------------|
| 1 | RSI | 0.274 | 38.5% | -32.2% | 7.7% | 100 |
| 2 | RSI | 0.218 | 31.0% | -36.2% | 10.0% | 100 |
| 3 | Mean Reversion | 0.216 | 13.7% | -20.3% | 1.9% | 100 |
| 4 | RSI | 0.213 | 16.7% | -26.7% | 3.8% | 100 |
| 5 | RSI | 0.199 | 37.1% | -39.6% | 13.0% | 100 |

**Key Finding:** RSI mean-reversion strategies outperformed trend-following approaches during the volatile 2014-2026 period (COVID crash, bull/bear markets).

## 🔍 Production Features

### Data Quality Monitoring
- ✅ **5 automated validation checks** (100% pass rate)
- ✅ **Completeness verification** - Null value detection
- ✅ **Price validity checks** - Anomaly detection
- ✅ **Data freshness tracking** - Staleness alerts
- ✅ **Coverage validation** - Stock consistency checks
- ✅ **OHLC logic verification** - Price relationship validation

### Performance Monitoring
- ✅ **Throughput tracking:** 240 backtests/second
- ✅ **Progress monitoring** with ETA calculation
- ✅ **Quality scoring** system (0-100 scale)
- ✅ **Automated alerting** for data issues
- ✅ **Real-time dashboards** for observability

### Technical Implementation
- ✅ **Parallel execution** with pandas UDFs
- ✅ **Smart data partitioning** by ticker
- ✅ **Comprehensive metrics** (Sharpe, Calmar, Drawdown, Win Rate)
- ✅ **Interactive visualizations** with Plotly
- ✅ **Scalable architecture** (designed for AWS EMR)

## 🛠️ Tech Stack

**Core Framework:**
- PySpark 3.5.0 (distributed computing)
- Python 3.12
- pandas (data manipulation)
- NumPy (numerical computing)

**Visualization:**
- Plotly (interactive dashboards)
- Matplotlib
- Seaborn

**Data:**
- yfinance (Yahoo Finance API)
- Parquet (columnar storage)

**Platform:**
- Kaggle Notebooks (30GB RAM)
- Designed for AWS EMR deployment

## 🚀 Quick Start

### Run on Kaggle (Recommended - 30GB RAM)
1. Open [`algorithmic-backtesting.ipynb`](algorithmic-backtesting.ipynb) on Kaggle
2. Enable **Internet** in notebook Settings
3. Run all cells (~30-60 minutes)
4. Interactive dashboards generated automatically

### Run on Google Colab (12GB RAM)
1. Open [`colab_quick_demo.ipynb`](colab_quick_demo.ipynb) on Colab
2. Run all cells (~15-30 minutes)
3. Smaller demo: 30 stocks, 3,690 backtests

### Run Locally
```bash
# Clone repository
git clone https://github.com/Het415/algorithmic-trading-backtest.git
cd algorithmic-trading-backtest

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook

# Open algorithmic-backtesting.ipynb
```

## 💡 Key Features

### Scale
- 123 trading strategies (MA, RSI, MACD, Mean Reversion)
- 100 stocks (major S&P 500 constituents)
- 10 years of real market data (2014-2026)
- Multiple market cycles tested (COVID crash, bull/bear markets)

### Technical Implementation
- **Distributed Processing:** PySpark with pandas UDFs for parallel execution
- **Data Partitioning:** By ticker to minimize shuffle operations
- **Quality Assurance:** 5-step automated validation pipeline
- **Performance Tracking:** Real-time monitoring with 240 tests/second throughput
- **Interactive Dashboards:** Plotly visualizations for analysis

### Key Insight
RSI strategies dominated top 5, demonstrating mean-reversion effectiveness during 2014-2026's regime changes and volatile market conditions.

## 🎓 What I Learned

- **Distributed Computing:** PySpark architecture, pandas UDFs, data partitioning strategies
- **Quantitative Finance:** Sharpe ratio, Calmar ratio, maximum drawdown, win rate metrics
- **Big Data Processing:** Handling 300K+ records efficiently with columnar storage
- **Data Quality Engineering:** Automated validation, anomaly detection, monitoring
- **Strategy Validation:** Testing across market cycles to prevent overfitting
- **Production Systems:** Quality assurance, monitoring, alerting, dashboards
- **Data Visualization:** Professional interactive dashboards with Plotly

## 📊 Technical Architecture

### Data Pipeline
```
Yahoo Finance API → Download (yfinance)
    ↓
Data Validation (5-step quality checks)
    ↓
Parquet Storage (partitioned by ticker)
    ↓
PySpark Loading (distributed dataframe)
    ↓
Strategy Grid Generation (123 strategies)
    ↓
Parallel Backtesting (pandas UDFs)
    ↓
Performance Aggregation
    ↓
Interactive Dashboards (Plotly)
```

### Monitoring System
- **Pre-Processing:** Data quality validation (completeness, validity, freshness)
- **During Processing:** Performance tracking (throughput, progress, ETA)
- **Post-Processing:** Strategy analysis (type comparison, performance distribution)
- **Visualization:** Real-time dashboards (quality scores, metrics, alerts)

## 🔮 Future Enhancements

- [ ] Deploy to AWS EMR for 500+ stock scale
- [ ] Add walk-forward analysis for robustness testing
- [ ] Implement transaction costs & slippage modeling
- [ ] Real-time backtesting with streaming data (Kafka)
- [ ] ML-based parameter optimization (Bayesian optimization)
- [ ] Portfolio optimization (combining multiple strategies)
- [ ] Automated strategy selection pipeline

## 📂 Project Structure
```
algorithmic-trading-backtest/
├── algorithmic-backtesting.ipynb              # Main Kaggle notebook (100 stocks)
├── colab_quick_demo.ipynb                     # Quick demo (30 stocks)
├── requirements.txt                           # Python dependencies
├── 3D visualization.png                       # Risk-return bubble chart
├── Complete Trading Backtesting analysis dash....png  # 9-panel dashboard
├── Strategy Type Performance Comparison.png   # Strategy type analysis
├── Top 15 trading strategies.png              # Top performers table
└── monitoring_dashboard.png                   # Production monitoring (NEW!)
```

## 🎯 Key Metrics

**Scale Metrics:**
- Strategies tested: 123
- Stocks analyzed: 100
- Total backtests: 12,300
- Price records: 303,600
- Time period: 10 years (2014-2026)

**Performance Metrics:**
- Best Sharpe ratio: 0.274
- Median Sharpe: 0.020
- Best return: 38.5%
- Max return: 675% (aggressive MA strategy)
- Throughput: 240 backtests/second

**Quality Metrics:**
- Data quality score: 100%
- Validation checks passed: 5/5
- Data completeness: 100%
- Price validity: ✅ Passed
- OHLC logic: ✅ Validated

## 💡 Technical Highlights

### Distributed Computing
- PySpark DataFrame operations
- pandas UDFs for vectorized time-series calculations
- Data partitioning by ticker for optimal performance
- Broadcast joins for strategy parameters

### Quantitative Finance
- Moving Average crossover strategies
- RSI mean-reversion strategies
- MACD momentum strategies  
- Bollinger Bands mean-reversion
- Comprehensive risk metrics (Sharpe, Calmar, Drawdown)

### Production Engineering
- Automated data quality validation
- Real-time performance monitoring
- Error detection and alerting
- Quality scoring system
- Interactive monitoring dashboards

## 📫 Contact

**Het415**


Linkedin : (https://www.linkedin.com/in/het-prajapati6210/)

Email: hetprajapati6210@gmail.com

Built: January 2026

---

⭐ **Star this repo if you found it useful!**

*This project demonstrates production-grade distributed systems engineering, quantitative finance knowledge, and professional software development practices.*
