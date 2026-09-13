from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_dashboard_smoke() -> None:
    dashboard_path = Path(__file__).resolve().parents[1] / "app" / "dashboard.py"

    app = AppTest.from_file(dashboard_path, default_timeout=10).run()

    assert not app.exception
    assert len(app.metric) == 3