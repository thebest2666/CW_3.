from src.classes import Operation
from src.utils import sort_operations, get_operations_executed, load_date


def test_get_operations_executed(date_operations):
    assert isinstance(get_operations_executed(date_operations)[0], dict)
    assert isinstance(get_operations_executed(date_operations), list)
    assert len(get_operations_executed(date_operations)) == 1


def test_cort_operations(operations):
    sorted_operations = sort_operations(operations)
    assert isinstance(sorted_operations, list)
    assert len(sorted_operations) > 0
    assert isinstance(sorted_operations[0], Operation)


def test_load_date(test_date):
    assert isinstance(test_date, list)
    assert isinstance(test_date[0], dict)