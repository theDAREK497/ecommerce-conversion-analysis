import pandas as pd
import pytest

from src.data_processing import (
    calculate_metrics,
    clean_data,
    conversion_by_device,
    load_data,
)


def test_sample_data_metrics() -> None:
    df = load_data("data/sample_data.csv")

    metrics = calculate_metrics(df)

    assert metrics["avg_page_load"] == pytest.approx(3.42)
    assert metrics["conversion_rate"] == pytest.approx(60.0)
    assert metrics["bounce_rate"] == pytest.approx(48.0)


def test_conversion_by_device() -> None:
    df = load_data("data/sample_data.csv")

    rates = conversion_by_device(df)

    assert rates["desktop"] == pytest.approx(100.0)
    assert rates["mobile"] == pytest.approx(0.0)


def test_clean_data_drops_incomplete_rows() -> None:
    df = pd.DataFrame(
        {
            "user_id": [1, 2],
            "device_type": ["desktop", None],
            "page_load_time_seconds": [2.0, 3.0],
            "bounce_rate": [0.2, 0.4],
            "conversion": [1, 0],
        }
    )

    cleaned = clean_data(df)

    assert len(cleaned) == 1
    assert str(cleaned["device_type"].dtype) == "category"


def test_missing_required_column_is_rejected() -> None:
    df = pd.DataFrame({"user_id": [1]})

    with pytest.raises(ValueError, match="Missing required columns"):
        clean_data(df)
