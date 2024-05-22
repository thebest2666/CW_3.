import json

from src.classes import Operation
from pathlib import Path


def load_date(path: Path):
    """
    Читаем файл данных нам операций
    """
    with open(path, encoding='utf-8') as operations:
        return json.load(operations)


def get_operations_executed(operation):
    """
    Фильтруем платежи на проведенные и нет
    """
    return [
        i for i in operation
        if i.get("state") == "EXECUTED" and i
    ]


def get_operations_instances(operations):
    """
    Заносим операции в список
    """
    operation_instances = []
    for operation in operations:
        operation_instance = Operation(
            state=operation["state"],
            date=operation["date"],
            amount=operation["operationAmount"]["amount"],
            corrency_name=operation["operationAmount"]["currency"]["name"],
            description=operation["description"],
            from_=operation.get("from"),
            to=operation["to"]
        )
        operation_instances.append(operation_instance)
    return operation_instances


def sort_operations(operations):
    """
    Сортируем операции
    """
    return sorted(operations, reverse=True)

