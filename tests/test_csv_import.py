from shoplite.csv_import import parse_file, parse_line


def test_parse_line():
    assert parse_line("A1, Mug, 9.50") == {"sku": "A1", "name": "Mug", "price": 9.5}


def test_comment_is_skipped():
    assert parse_line("# header") is None


def test_parse_file():
    assert len(parse_file("A1,Mug,9.5\nB2,Cup,3")) == 2
