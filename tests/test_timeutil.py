from datetime import datetime

from shoplite.timeutil import to_utc


def test_utc_is_unchanged():
    assert to_utc("2026-01-01T12:00:00", "UTC") == datetime(2026, 1, 1, 12, 0)
