"""Time helpers. All order timestamps are stored in UTC."""
from datetime import datetime, timedelta

# Fixed UTC offsets (hours) for the stores we operate. No DST handling needed.
STORE_OFFSETS = {
    "UTC": 0,
    "IST": 5.5,   # India, UTC+05:30
    "EST": -5,    # New York (winter), UTC-05:00
    "JST": 9,     # Tokyo, UTC+09:00
}


def to_utc(local_iso, tz):
    """Convert a naive local ISO timestamp from store ``tz`` to a naive UTC datetime.

    >>> to_utc("2026-01-01T12:00:00", "UTC")
    datetime.datetime(2026, 1, 1, 12, 0)
    """
    if tz not in STORE_OFFSETS:
        raise KeyError(f"unknown store timezone: {tz}")
    local = datetime.fromisoformat(local_iso)
    return local + timedelta(hours=STORE_OFFSETS[tz])
