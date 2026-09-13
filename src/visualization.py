import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure

from src.data_processing import conversion_by_device


def plot_conversion_by_device(df: pd.DataFrame) -> Figure:
    rates = conversion_by_device(df)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(rates.index.astype(str), rates.values)
    ax.set_title("Conversion Rate by Device Type")
    ax.set_xlabel("Device type")
    ax.set_ylabel("Conversion rate (%)")
    ax.set_ylim(0, 100)
    fig.tight_layout()
    return fig


def plot_page_load_vs_bounce(df: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(figsize=(8, 5))

    for device_type, group in df.groupby("device_type", observed=True):
        ax.scatter(
            group["page_load_time_seconds"],
            group["bounce_rate"] * 100,
            label=str(device_type),
        )

    ax.set_title("Page Load Time vs Bounce Rate")
    ax.set_xlabel("Page load time (seconds)")
    ax.set_ylabel("Bounce rate (%)")
    ax.legend(title="Device type")
    fig.tight_layout()
    return fig
