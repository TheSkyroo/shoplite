from shoplite.pagination import page_count


def test_page_count():
    assert page_count(25, 10) == 3
    assert page_count(0, 10) == 0
