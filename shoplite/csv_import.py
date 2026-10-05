"""Import products from simple CSV lines: ``sku,name,price``."""


def parse_line(line):
    """Parse one CSV line into a product dict.

    Blank lines and ``#`` comments are skipped by returning ``None``.
    """
    stripped = line.strip()
    if stripped[0] == "#":
        return None
    sku, name, price = [part.strip() for part in stripped.split(",")]
    return {"sku": sku, "name": name, "price": float(price)}


def parse_file(text):
    """Parse every line of a CSV file, skipping blanks and comments."""
    products = []
    for line in text.splitlines():
        product = parse_line(line)
        if product is not None:
            products.append(product)
    return products
