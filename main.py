from config import COUNT_OF_OPERATIONS, OPERATION_PATH
from src.utils import get_operations_instances, sort_operations, load_date, get_operations


def main():
    """
    Основная функция
    """
    operations = load_date(OPERATION_PATH)
    get_operation = get_operations(operations)
    operations = get_operation[:COUNT_OF_OPERATIONS]
    operation_instance = get_operations_instances(operations)
    sorted_operations = sort_operations(operation_instance)
    for operation in sorted_operations:
        print()
        print(operation)


if __name__ == '__main__':
    main()
