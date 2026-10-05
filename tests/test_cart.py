from shoplite.cart import subtotal, total

LINES = [{"price": 10.0, "qty": 2}, {"price": 5.5, "qty": 1}]


def test_subtotal():
    assert subtotal(LINES) == 25.5


def test_total_with_discount_and_tax():
    assert total(LINES, discount_pct=10, tax_pct=10) == 25.25
