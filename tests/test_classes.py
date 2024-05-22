def test_init_operation(operation):
    assert operation.from_ == ""


def test_convert_date(operation):
    assert isinstance(operation.convert_date(), str)
    assert operation.convert_date() == "26.08.2019"


def test_operation_str(operation):
    assert str(operation) == f"26.08.2019 Перевод организации\nСчет **9589\n31957.58 руб."
