import streamlit as st
from dashboard.data.loader import load_results
from dashboard.components.charts import build_3d_scatter, build_top_table

st.header("Strategy Explorer")
st.caption("Interact with the 3D chart: rotate by dragging, zoom with scroll, hover for details.")

df = load_results()

# ── Sidebar filters ───────────────────────────────────────────────────────────
st.sidebar.subheader("Filters")

all_types = sorted(df["strategy_type"].unique())
selected_types = st.sidebar.multiselect(
    "Strategy types",
    options=all_types,
    default=all_types,
    format_func=lambda x: x.replace("_", " ").title(),
)

sharpe_min, sharpe_max = float(df["avg_sharpe"].min()), float(df["avg_sharpe"].max())
sharpe_range = st.sidebar.slider(
    "Sharpe ratio range",
    min_value=round(sharpe_min, 2),
    max_value=round(sharpe_max, 2),
    value=(round(sharpe_min, 2), round(sharpe_max, 2)),
    step=0.01,
)

dd_min, dd_max = float(df["avg_drawdown"].min() * 100), float(df["avg_drawdown"].max() * 100)
dd_range = st.sidebar.slider(
    "Max drawdown range (%)",
    min_value=round(dd_min, 1),
    max_value=round(dd_max, 1),
    value=(round(dd_min, 1), round(dd_max, 1)),
    step=0.5,
)

top_n = st.sidebar.slider("Top-N strategies in table", min_value=5, max_value=30, value=15, step=5)

# Apply filters
mask = (
    df["strategy_type"].isin(selected_types)
    & df["avg_sharpe"].between(sharpe_range[0], sharpe_range[1])
    & (df["avg_drawdown"] * 100).between(dd_range[0], dd_range[1])
)
filtered = df[mask]

st.caption(f"Showing **{len(filtered)}** of {len(df)} strategies")

if filtered.empty:
    st.warning("No strategies match the current filters. Adjust the sliders in the sidebar.")
    st.stop()

# ── 3D scatter ────────────────────────────────────────────────────────────────
st.plotly_chart(build_3d_scatter(filtered), use_container_width=True)

st.divider()

# ── Top-N table ───────────────────────────────────────────────────────────────
st.subheader(f"Top {top_n} Strategies (filtered)")
st.plotly_chart(build_top_table(filtered, n=top_n), use_container_width=True)
