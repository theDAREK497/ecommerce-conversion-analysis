from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "user_id",
    "device_type",
    "page_load_time_seconds",
    "bounce_rate",
    "conversion",
}


def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Missing required columns: {missing_list}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)

    cleaned = df.dropna(subset=sorted(REQUIRED_COLUMNS)).copy()
    cleaned["device_type"] = cleaned["device_type"].astype("category")
    return cleaned


def load_data(filepath: str | Path) -> pd.DataFrame:
    return clean_data(pd.read_csv(filepath))


def calculate_metrics(df: pd.DataFrame) -> dict[str, float]:
    validate_columns(df)
    if df.empty:
        raise ValueError("Cannot calculate metrics for an empty dataset")

    return {
        "avg_page_load": float(df["page_load_time_seconds"].mean()),
        "conversion_rate": float(df["conversion"].mean() * 100),
        "bounce_rate": float(df["bounce_rate"].mean() * 100),
    }


def conversion_by_device(df: pd.DataFrame) -> pd.Series:
    validate_columns(df)
    return (
        df.groupby("device_type", observed=True)["conversion"]
        .mean()
        .mul(100)
        .sort_index()
    )
