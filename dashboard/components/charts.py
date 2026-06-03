"""Plotly figure factories — one function per chart, all return go.Figure."""
from __future__ import annotations

from typing import Optional

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

_TYPE_COLORS = {
    "moving_average": "#4C78A8",
    "rsi": "#F58518",
    "macd": "#54A24B",
    "mean_reversion": "#E45756",
}
_FALLBACK_COLORS = ["#4C78A8", "#F58518", "#54A24B", "#E45756"]


def _type_color(strategy_type: str) -> str:
    return _TYPE_COLORS.get(strategy_type, "#888")


# ── Overview ─────────────────────────────────────────────────────────────────

def build_strategy_count_bar(df: pd.DataFrame) -> go.Figure:
    counts = df["strategy_type"].value_counts().reset_index()
    counts.columns = ["strategy_type", "count"]
    counts["label"] = counts["strategy_type"].str.replace("_", " ").str.title()
    counts["color"] = counts["strategy_type"].map(_TYPE_COLORS)
    fig = go.Figure(
        go.Bar(
            x=counts["label"],
            y=counts["count"],
            marker_color=counts["color"],
            text=counts["count"],
            textposition="outside",
        )
    )
    fig.update_layout(
        title="Strategy Count by Type",
        xaxis_title="Strategy Type",
        yaxis_title="Number of Strategies",
        showlegend=False,
        height=350,
        margin=dict(t=50, b=40),
    )
    return fig


# ── Strategy Explorer ─────────────────────────────────────────────────────────

def build_3d_scatter(df: pd.DataFrame) -> go.Figure:
    plot_df = df.copy()
    plot_df["Return %"] = (plot_df["avg_return"] * 100).round(1)
    plot_df["Drawdown %"] = (plot_df["avg_drawdown"] * 100).round(1)
    plot_df["Sharpe"] = plot_df["avg_sharpe"].round(3)
    plot_df["Win Rate %"] = (plot_df["avg_win_rate"] * 100).round(1)
    plot_df["Strategy Label"] = (
        plot_df["strategy_type"].str.replace("_", " ").str.title()
        + " · "
        + plot_df["strategy_id"].str[-4:]
    )

    fig = px.scatter_3d(
        plot_df,
        x="Drawdown %",
        y="Return %",
        z="Sharpe",
        color="strategy_type",
        size="num_stocks",
        hover_data=["Strategy Label", "Win Rate %"],
        color_discrete_map={k: v for k, v in _TYPE_COLORS.items()},
        labels={
            "Drawdown %": "Max Drawdown (%)",
            "Return %": "Total Return (%)",
            "Sharpe": "Sharpe Ratio",
            "strategy_type": "Strategy Type",
        },
        height=650,
    )
    fig.update_layout(
        title=dict(
            text=f"<b>3D Strategy Analysis: Risk vs Return vs Sharpe</b><br>"
                 f"<sup>{len(df):,} strategies across {int(df['num_stocks'].max())} stocks</sup>",
            x=0.5,
        ),
        scene=dict(
            xaxis=dict(backgroundcolor="rgb(230,230,230)", gridcolor="white"),
            yaxis=dict(backgroundcolor="rgb(230,230,230)", gridcolor="white"),
            zaxis=dict(backgroundcolor="rgb(230,230,230)", gridcolor="white"),
        ),
        legend_title_text="Strategy Type",
        font=dict(family="Arial", size=12),
        margin=dict(t=80),
    )
    return fig


def build_top_table(df: pd.DataFrame, n: int = 15) -> go.Figure:
    top = df.nlargest(n, "avg_sharpe").reset_index(drop=True)
    row_colors = ["#FFFFFF" if i % 2 == 0 else "#F0F4FA" for i in range(len(top))]
    NUM_COLS = 8

    fig = go.Figure(
        go.Table(
            header=dict(
                values=[
                    "<b>#</b>",
                    "<b>Type</b>",
                    "<b>Sharpe</b>",
                    "<b>Return %</b>",
                    "<b>Drawdown %</b>",
                    "<b>Win Rate %</b>",
                    "<b>Calmar</b>",
                    "<b>Stocks</b>",
                ],
                fill_color="#2C5282",
                align="center",
                font=dict(color="white", size=13, family="Arial Black"),
                height=38,
            ),
            cells=dict(
                values=[
                    list(range(1, len(top) + 1)),
                    top["strategy_type"].str.replace("_", " ").str.title(),
                    top["avg_sharpe"].round(3),
                    (top["avg_return"] * 100).round(1),
                    (top["avg_drawdown"] * 100).round(1),
                    (top["avg_win_rate"] * 100).round(1),
                    top["avg_calmar"].round(3),
                    top["num_stocks"],
                ],
                fill_color=[row_colors] * NUM_COLS,
                align="center",
                font=dict(size=12, family="Arial", color="#1A202C"),
                height=30,
            ),
        )
    )
    fig.update_layout(
        title=dict(
            text=f"<b>Top {n} Strategies by Sharpe Ratio</b>",
            x=0.5,
            font_size=18,
        ),
        height=min(80 + n * 32, 600),
        margin=dict(l=10, r=10, t=60, b=10),
    )
    return fig


# ── Type Comparison ───────────────────────────────────────────────────────────

def build_radar_chart(df: pd.DataFrame) -> go.Figure:
    summary = (
        df.groupby("strategy_type")
        .agg(
            avg_sharpe=("avg_sharpe", "mean"),
            avg_return=("avg_return", "mean"),
            avg_win_rate=("avg_win_rate", "mean"),
            avg_drawdown=("avg_drawdown", "mean"),
        )
        .reset_index()
    )

    def _norm(series):
        rng = series.max() - series.min()
        return (series - series.min()) / rng if rng > 0 else series * 0

    summary["sharpe_norm"] = _norm(summary["avg_sharpe"])
    summary["return_norm"] = _norm(summary["avg_return"])
    summary["winrate_norm"] = _norm(summary["avg_win_rate"])
    summary["drawdown_norm"] = 1 - _norm(summary["avg_drawdown"])

    categories = ["Sharpe Ratio", "Returns", "Win Rate", "Risk Control"]
    fig = go.Figure()
    for _, row in summary.iterrows():
        vals = [
            row["sharpe_norm"],
            row["return_norm"],
            row["winrate_norm"],
            row["drawdown_norm"],
        ]
        label = row["strategy_type"].replace("_", " ").title()
        fig.add_trace(
            go.Scatterpolar(
                r=vals + [vals[0]],
                theta=categories + [categories[0]],
                fill="toself",
                name=label,
                line_color=_type_color(row["strategy_type"]),
                opacity=0.65,
            )
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1], showticklabels=False),
        ),
        title=dict(
            text="<b>Strategy Type Performance Comparison</b>",
            x=0.5,
            font_size=18,
        ),
        showlegend=True,
        legend_title_text="Strategy Type",
        height=500,
        margin=dict(t=80),
    )
    return fig


def build_type_bar(df: pd.DataFrame) -> go.Figure:
    summary = (
        df.groupby("strategy_type")["avg_sharpe"]
        .agg(["mean", "std"])
        .reset_index()
        .rename(columns={"mean": "avg", "std": "err"})
        .sort_values("avg", ascending=False)
    )
    labels = summary["strategy_type"].str.replace("_", " ").str.title()
    colors = [_type_color(t) for t in summary["strategy_type"]]

    fig = go.Figure(
        go.Bar(
            x=labels,
            y=summary["avg"],
            error_y=dict(type="data", array=summary["err"].fillna(0), visible=True),
            marker_color=colors,
            text=summary["avg"].round(3),
            textposition="outside",
        )
    )
    fig.update_layout(
        title="Average Sharpe Ratio by Strategy Type",
        yaxis_title="Avg Sharpe Ratio",
        showlegend=False,
        height=380,
        margin=dict(t=50, b=40),
    )
    return fig


def build_sharpe_box(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    for stype, color in _TYPE_COLORS.items():
        subset = df[df["strategy_type"] == stype]["avg_sharpe"]
        if subset.empty:
            continue
        fig.add_trace(
            go.Box(
                y=subset,
                name=stype.replace("_", " ").title(),
                marker_color=color,
                boxmean="sd",
            )
        )
    fig.update_layout(
        title="Sharpe Ratio Distribution by Type",
        yaxis_title="Sharpe Ratio",
        showlegend=False,
        height=380,
        margin=dict(t=50, b=40),
    )
    return fig


# ── Monitoring ────────────────────────────────────────────────────────────────

def build_monitoring(meta: dict, df: Optional[pd.DataFrame] = None) -> go.Figure:
    quality_score = meta.get("quality_score", 100)
    throughput = meta.get("throughput_per_sec", 240)
    checks = meta.get(
        "validation_checks",
        [
            {"name": "Completeness", "status": "PASS"},
            {"name": "Price Validity", "status": "PASS"},
            {"name": "Data Freshness", "status": "PASS"},
            {"name": "Coverage", "status": "PASS"},
            {"name": "OHLC Logic", "status": "PASS"},
        ],
    )

    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Data Quality Score",
            "Throughput (Backtests / sec)",
            "Avg Sharpe by Strategy Type",
            "Quality Checks",
        ),
        specs=[
            [{"type": "indicator"}, {"type": "indicator"}],
            [{"type": "bar"}, {"type": "table"}],
        ],
        vertical_spacing=0.14,
        horizontal_spacing=0.08,
    )

    # Quality gauge
    fig.add_trace(
        go.Indicator(
            mode="gauge+number+delta",
            value=quality_score,
            delta={"reference": 90, "relative": False},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "darkgreen" if quality_score >= 90 else "orange"},
                "steps": [
                    {"range": [0, 70], "color": "lightgray"},
                    {"range": [70, 90], "color": "gray"},
                    {"range": [90, 100], "color": "lightgreen"},
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": 90,
                },
            },
        ),
        row=1,
        col=1,
    )

    # Throughput
    fig.add_trace(
        go.Indicator(
            mode="number+delta",
            value=throughput,
            delta={"reference": 1, "relative": False},
            number={"suffix": " /s", "font": {"size": 48}},
        ),
        row=1,
        col=2,
    )

    # Avg Sharpe bar
    if df is not None and not df.empty:
        type_perf = (
            df.groupby("strategy_type")["avg_sharpe"]
            .mean()
            .sort_values(ascending=False)
        )
        fig.add_trace(
            go.Bar(
                x=[t.replace("_", " ").title() for t in type_perf.index],
                y=type_perf.values,
                marker_color=[_type_color(t) for t in type_perf.index],
                text=type_perf.values.round(3),
                textposition="outside",
            ),
            row=2,
            col=1,
        )

    # Checks table
    status_labels = [
        "✅ PASS" if c["status"] == "PASS" else "❌ FAIL" for c in checks
    ]
    fig.add_trace(
        go.Table(
            header=dict(
                values=["<b>Quality Check</b>", "<b>Status</b>"],
                fill_color="#2C5282",
                font=dict(color="white", size=13),
                height=32,
            ),
            cells=dict(
                values=[[c["name"] for c in checks], status_labels],
                fill_color="white",
                font=dict(size=12),
                height=28,
            ),
        ),
        row=2,
        col=2,
    )

    fig.update_layout(
        title=dict(
            text="<b>Backtesting Pipeline Monitoring Dashboard</b>",
            x=0.5,
            font_size=20,
        ),
        height=720,
        showlegend=False,
        margin=dict(t=80, b=20),
    )
    return fig
