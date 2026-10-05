"""Shopping cart totals."""


def subtotal(lines):
    """Sum of ``price * qty`` over cart lines (dicts with price and qty)."""
    return round(sum(line["price"] * line["qty"] for line in lines), 2)


def total(lines, discount_pct=0, tax_pct=0):
    """Cart total after a percentage discount, then tax on the discounted amount."""
    if not 0 <= discount_pct <= 100:
        raise ValueError("discount_pct must be between 0 and 100")
    discounted = subtotal(lines) * (1 - discount_pct / 100)
    return round(discounted * (1 + tax_pct / 100), 2)
