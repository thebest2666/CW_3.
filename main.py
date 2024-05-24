from config import OPERATION_PATH, OPERATIONS_COUNT
from src.utils import get_operations_instances, sort_operations, load_date, get_operations_executed


def main():
    """
    Основная функция
    """
    operations = load_date(OPERATION_PATH)
    operations_executed = get_operations_executed(operations)
    operation_instance = get_operations_instances(operations_executed)
    sorted_operations = sort_operations(operation_instance)
    selected_operations = sorted_operations[:OPERATIONS_COUNT]
    for operation in selected_operations:
        print()
        print(operation)


if __name__ == '__main__':
    main()
