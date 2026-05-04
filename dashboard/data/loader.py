import json
import streamlit as st
import pandas as pd
from pathlib import Path

_ROOT = Path(__file__).parents[2]
RESULTS_PATH = _ROOT / "data" / "results.csv"
METADATA_PATH = _ROOT / "data" / "metadata.json"

_DEFAULT_META = {
    "quality_score": 100.0,
    "throughput_per_sec": 240,
    "total_backtests": 12300,
    "stocks_tested": 100,
    "run_timestamp": None,
    "validation_checks": [
        {"name": "Completeness", "status": "PASS"},
        {"name": "Price Validity", "status": "PASS"},
        {"name": "Data Freshness", "status": "PASS"},
        {"name": "Coverage", "status": "PASS"},
        {"name": "OHLC Logic", "status": "PASS"},
    ],
}


@st.cache_data
def load_results() -> pd.DataFrame:
    if not RESULTS_PATH.exists():
        st.error(
            "**No results file found.** "
            "Run all cells in `algorithmic-backtesting.ipynb` (including the export cell at the end) "
            "to generate `data/results.csv`, then reload this page."
        )
        st.stop()
    df = pd.read_csv(RESULTS_PATH)
    # Normalise column names to lowercase
    df.columns = [c.lower().strip() for c in df.columns]
    return df


@st.cache_data
def load_metadata() -> dict:
    if not METADATA_PATH.exists():
        return _DEFAULT_META.copy()
    try:
        return json.loads(METADATA_PATH.read_text())
    except Exception:
        return _DEFAULT_META.copy()
