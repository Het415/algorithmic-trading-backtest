import streamlit as st
from dashboard.data.loader import load_results, load_metadata
from dashboard.components.charts import build_strategy_count_bar

st.header("Overview")

df = load_results()
meta = load_metadata()

# ── KPI cards ─────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)

total_backtests = meta.get("total_backtests", len(df))
best_sharpe = df["avg_sharpe"].max()
best_return = df["avg_return"].max() * 100
avg_drawdown = df["avg_drawdown"].mean() * 100

c1.metric("Total Backtests", f"{total_backtests:,}")
c2.metric("Best Sharpe Ratio", f"{best_sharpe:.3f}")
c3.metric("Best Total Return", f"{best_return:.1f}%")
c4.metric("Avg Max Drawdown", f"{avg_drawdown:.1f}%")

st.divider()

# ── Strategy count bar + quick stats ─────────────────────────────────────────
col_chart, col_stats = st.columns([2, 1])

with col_chart:
    st.plotly_chart(build_strategy_count_bar(df), use_container_width=True)

with col_stats:
    st.subheader("Quick Stats")
    st.write(f"**Strategies tested:** {len(df)}")
    st.write(f"**Stocks covered:** {int(df['num_stocks'].max())}")
    st.write(f"**Median Sharpe:** {df['avg_sharpe'].median():.3f}")
    st.write(f"**Strategies (Sharpe > 0.2):** {(df['avg_sharpe'] > 0.2).sum()}")
    st.write(f"**Strategies (Sharpe > 0.3):** {(df['avg_sharpe'] > 0.3).sum()}")

    run_ts = meta.get("run_timestamp")
    if run_ts:
        st.caption(f"Last backtest run: {run_ts[:19].replace('T', ' ')}")

st.divider()

# ── Per-type summary table ────────────────────────────────────────────────────
st.subheader("Performance Summary by Strategy Type")
summary = (
    df.groupby("strategy_type")
    .agg(
        Count=("avg_sharpe", "count"),
        Best_Sharpe=("avg_sharpe", "max"),
        Avg_Sharpe=("avg_sharpe", "mean"),
        Best_Return=("avg_return", "max"),
        Avg_Drawdown=("avg_drawdown", "mean"),
    )
    .reset_index()
    .rename(columns={"strategy_type": "Strategy Type"})
)
summary["Strategy Type"] = summary["Strategy Type"].str.replace("_", " ").str.title()
summary["Best_Return"] = (summary["Best_Return"] * 100).round(1).astype(str) + "%"
summary["Avg_Drawdown"] = (summary["Avg_Drawdown"] * 100).round(1).astype(str) + "%"
summary["Best_Sharpe"] = summary["Best_Sharpe"].round(3)
summary["Avg_Sharpe"] = summary["Avg_Sharpe"].round(3)
summary.columns = ["Strategy Type", "Count", "Best Sharpe", "Avg Sharpe", "Best Return", "Avg Drawdown"]
st.dataframe(summary, use_container_width=True, hide_index=True)
