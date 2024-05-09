from typing import Callable

from src.operation_validators import OperationValidator


class FinancialWallet:
    """
    Класс личного финансового кошелька
    """
    def __init__(self, data: list[dict[str, str | int]]) -> None:
        """
        Инициализация кошелька с данными операций.
        :param data: Данные операций в виде списка словарей
        """
        self.data: list[dict[str, str | int]] = data
        if not data:
            self.id_counter: int = 1
        else:
            self.id_counter: int = max(op.get('id', 1) for op in data) + 1

    def __str__(self) -> str:
        balance, income, expenses = self.get_balance()
        return f'\nБаланс вашего кошелька: {balance}\nДоход: {income}\nРасход: {expenses}\n'

    def add_operation(self, operation_data: dict[str, str | int]) -> None:
        """
        Добавляет новую операцию в кошелек.
        :param operation_data: Данные новой операции.
        """
        operation_data['id'] = self.id_counter
        self.data.append(operation_data)
        self.id_counter += 1

    def edit_operation(self, operation_id: int, updated_data: dict[str, [str, str | int]]) -> None:
        """
        Редактирует операцию по её идентификатору.
        :param operation_id: Идентификатор операции
        :param updated_data: Обновлённые данные операции.
        """
        for operation in self.data:
            if operation.get('id') == operation_id:
                operation.update(updated_data)

    def search_operation(self, validator: OperationValidator) -> list[dict[str, [str, str | int]]]:
        """
        Ищет операции по заданным критериям.
        :param validator: Объект валидатора.
        :return: Найденные операции.
        """
        categories: dict[str, str] = {
            'дата': 'date',
            'категория': 'category',
            'сумма': 'amount'
        }
        search_key: str = validator.get_validated_search_key(categories)

        validate_value: dict[str, Callable] = {
            'date': validator.get_validated_date,
            'category': validator.get_validated_category,
            'amount': validator.get_validated_amount
        }
        search_value: str = validate_value.get(search_key)()
        results: list = [operation for operation in self.data if operation.get(search_key) == search_value]

        return results

    def get_balance(self) -> tuple[int, int, int]:
        """
        Рассчитывает баланс кошелька.
        :return: Баланс кошелька, доходы, расходы.
        """
        income: int = sum(
            operation.get('amount', 0) for operation in self.data if operation.get('category') == 'доход'
        )
        expenses: int = sum(
            operation.get('amount', 0) for operation in self.data if operation.get('category') == 'расход'
        )
        balance: int = income - expenses
        return balance, income, expenses
