import pytest

from config import OPERATION_PATH
from src.classes import Operation
from src.utils import load_date


@pytest.fixture
def operation():
    return Operation(
        state="EXECUTED",
        date="2019-08-26T10:50:58.294041",
        amount="31957.58",
        corrency_name="руб.",
        description="Перевод организации",
        from_=None,
        to="Счет 64686473678894779589"
    )


@pytest.fixture
def operations():
    return [
        Operation(
            state="EXECUTED",
            date="2019-08-26T10:50:58.294041",
            amount="31957.58",
            corrency_name="руб.",
            description="Перевод организации",
            from_=None,
            to="Счет 64686473678894779589"
        ),
        Operation(
            state="CANCELED",
            date="2019-07-03T18:35:29.512364",
            amount="8221.37",
            corrency_name="USD",
            description="Перевод организации",
            from_="MasterCard 7158300734726758",
            to="Счет 35383033474447895560"
        ),
        Operation(
            state="EXECUTED",
            date="2019-08-26T10:50:58.294041",
            amount="31957.58",
            corrency_name="руб.",
            description="Перевод организации",
            from_=None,
            to="Счет 64686473678894779589"
        )
    ]


@pytest.fixture
def date_operations():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]


@pytest.fixture
def test_date():
    data = load_date(OPERATION_PATH)
    return data
