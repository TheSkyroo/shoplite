"""Pagination helpers for list endpoints."""


def paginate(items, page, per_page=10):
    """Return the items on a 1-based ``page``.

    >>> paginate(list(range(25)), 1, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if page < 1:
        raise ValueError("page must be >= 1")
    if per_page < 1:
        raise ValueError("per_page must be >= 1")
    start = page * per_page - per_page + 1
    return items[start:start + per_page]


def page_count(total, per_page=10):
    """Number of pages needed to show ``total`` items."""
    if per_page < 1:
        raise ValueError("per_page must be >= 1")
    return (total + per_page - 1) // per_page
