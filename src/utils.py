from datetime import datetime
from typing import Any, Callable

from src.financial_wallet import FinancialWallet
from src.operation_validators import OperationValidator


def display_operation_info(result: dict[str, Any]) -> None:
    """
    Выводит информацию об операции.
    :param result: Словарь с информацией об операции.
    """
    operation_id: int = result.get('id')
    date: str = result.get('date')
    category: str = result.get('category')
    amount: int = result.get('amount')
    description: str = result.get('description')
    print(f'\nid: {operation_id}\nДата: {date}\nКатегория: {category.capitalize()}\n'
          f'Сумма: {amount}\nОписание: {description}\n')


def add_operation(wallet: FinancialWallet, validator: OperationValidator) -> None:
    """
     Добавляет операцию.
    :param wallet: Кошелек.
    :param validator: Валидатор данных.
    """
    operation_data: dict[str, Any] = {
        'date': str(datetime.now().date()),
        'category': validator.get_validated_category(),
        'amount': validator.get_validated_amount(),
        'description': input('Введите описание: ')
    }
    wallet.add_operation(operation_data)


def edit_operation(wallet: FinancialWallet, validator: OperationValidator) -> None:
    """
    Редактирует операцию.
    :param wallet: Кошелек.
    :param validator: Валидатор данных.
    """
    operation_data: dict[str, Callable] = {
        'date': validator.get_validated_date,
        'category': validator.get_validated_category,
        'amount': validator.get_validated_amount,
        'description': lambda: input('Введите новое описание: ')
    }

    results: list[dict[str, str | int]] = wallet.search_operation(validator)
    if results:
        for result in results:
            display_operation_info(result)

        operation_id: int = validator.get_validated_id_input()
        field_name: str = validator.get_validated_field_input()
        updated_value: str = operation_data.get(field_name)()
        updated_data: dict[str, str | int] = {field_name: updated_value}
        wallet.edit_operation(operation_id, updated_data)

    else:
        print('Записи не найдены.')


def search_operations(wallet: FinancialWallet, validator: OperationValidator) -> list[dict[str, str | int]]:
    """
    Поиск операции.

    :param wallet: Кошелек.
    :param validator: Валидатор данных.
    :return: Список операций.
    """
    results: list[dict[str, str | int]] = wallet.search_operation(validator)
    if results:
        for result in results:
            display_operation_info(result)
        return results
    else:
        print('Результаты не найдены.')
