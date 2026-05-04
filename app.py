import streamlit as st

st.set_page_config(
    page_title="Algorithmic Trading Backtesting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = {
    "Dashboard": [
        st.Page(
            "dashboard/pages/overview.py",
            title="Overview",
            icon=":material/dashboard:",
        ),
        st.Page(
            "dashboard/pages/strategy_explorer.py",
            title="Strategy Explorer",
            icon=":material/scatter_plot:",
        ),
        st.Page(
            "dashboard/pages/type_comparison.py",
            title="Type Comparison",
            icon=":material/radar:",
        ),
        st.Page(
            "dashboard/pages/monitoring.py",
            title="Monitoring",
            icon=":material/monitor_heart:",
        ),
    ]
}

pg = st.navigation(pages)

with st.sidebar:
    st.title("📈 Algo Backtesting")
    st.caption(
        "Interactive dashboard for 12,300 backtests across "
        "100 S&P 500 stocks and 123 strategies."
    )
    st.divider()
    st.caption(
        "**How to use:** Run the notebook (`algorithmic-backtesting.ipynb`) "
        "including the export cell to generate `data/results.csv`, "
        "then reload this page."
    )

pg.run()
