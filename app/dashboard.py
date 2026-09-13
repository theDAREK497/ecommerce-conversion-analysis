import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, os.fspath(ROOT_DIR))

import streamlit as st  # noqa: E402

from src.data_processing import calculate_metrics, load_data  # noqa: E402
from src.visualization import (  # noqa: E402
    plot_conversion_by_device,
    plot_page_load_vs_bounce,
)

DATA_PATH = ROOT_DIR / "data" / "sample_data.csv"

st.set_page_config(page_title="E-commerce Conversion Analysis", layout="wide")
st.title("E-commerce Conversion Analysis")
st.caption("Sample analytics dashboard for website performance and conversion metrics.")

df = load_data(DATA_PATH)
metrics = calculate_metrics(df)

metric_columns = st.columns(3)
metric_columns[0].metric(
    "Average page load",
    f"{metrics['avg_page_load']:.2f} s",
)
metric_columns[1].metric(
    "Conversion rate",
    f"{metrics['conversion_rate']:.1f}%",
)
metric_columns[2].metric(
    "Bounce rate",
    f"{metrics['bounce_rate']:.1f}%",
)

st.subheader("Conversion by device")
st.pyplot(plot_conversion_by_device(df))

st.subheader("Page load time vs bounce rate")
st.pyplot(plot_page_load_vs_bounce(df))

st.subheader("Source data")
st.dataframe(df, use_container_width=True)
