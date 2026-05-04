import streamlit as st
from dashboard.data.loader import load_results
from dashboard.components.charts import build_radar_chart, build_type_bar, build_sharpe_box

st.header("Strategy Type Comparison")

df = load_results()

# ── Radar chart ───────────────────────────────────────────────────────────────
st.plotly_chart(build_radar_chart(df), use_container_width=True)

st.divider()

# ── Bar + box side-by-side ────────────────────────────────────────────────────
col_bar, col_box = st.columns(2)

with col_bar:
    st.plotly_chart(build_type_bar(df), use_container_width=True)

with col_box:
    st.plotly_chart(build_sharpe_box(df), use_container_width=True)

st.divider()

# ── Detailed per-type stats ───────────────────────────────────────────────────
st.subheader("Detailed Statistics by Type")

summary = (
    df.groupby("strategy_type")
    .agg(
        Strategies=("avg_sharpe", "count"),
        Avg_Sharpe=("avg_sharpe", "mean"),
        Median_Sharpe=("avg_sharpe", "median"),
        Best_Sharpe=("avg_sharpe", "max"),
        Avg_Return=("avg_return", "mean"),
        Avg_Win_Rate=("avg_win_rate", "mean"),
        Avg_Drawdown=("avg_drawdown", "mean"),
    )
    .reset_index()
)

summary["strategy_type"] = summary["strategy_type"].str.replace("_", " ").str.title()
for col in ["Avg_Sharpe", "Median_Sharpe", "Best_Sharpe"]:
    summary[col] = summary[col].round(3)
for col in ["Avg_Return", "Avg_Win_Rate", "Avg_Drawdown"]:
    summary[col] = (summary[col] * 100).round(1).astype(str) + "%"

summary.columns = [
    "Strategy Type", "Strategies",
    "Avg Sharpe", "Median Sharpe", "Best Sharpe",
    "Avg Return", "Avg Win Rate", "Avg Drawdown",
]
st.dataframe(summary, use_container_width=True, hide_index=True)
