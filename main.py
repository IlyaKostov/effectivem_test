import os

from src.file_manager import FileManager
from src.financial_wallet import FinancialWallet
from src.operation_validators import OperationValidator
from src.utils import add_operation, search_operations, edit_operation

WALLET_DATA = 'my_wallet.json'


def main():
    filepath = os.path.join(os.path.dirname(__file__), WALLET_DATA)
    data_manager = FileManager(filepath)
    data = data_manager.load_data()
    wallet = FinancialWallet(data)

    validator = OperationValidator()

    try:
        while True:
            actions = {
                '1': lambda: print(wallet),
                '2': lambda: add_operation(wallet, validator),
                '3': lambda: edit_operation(wallet, validator),
                '4': lambda: search_operations(wallet, validator),
            }

            print('\n"Личный кошелек"')
            print('1. Вывод баланса')
            print('2. Добавление записи')
            print('3. Редактирование записи')
            print('4. Поиск по записям')
            print('5. Выход')

            choice = input('Выберите действие: ')

            if choice == '5':
                data_manager.save_data(wallet.data)
                print('Данные сохранены. Программа завершена.')
                break

            action = actions.get(choice)
            if action:
                action()
            else:
                print('Некорректный выбор. Попробуйте снова.')
    except KeyboardInterrupt:
        data_manager.save_data(wallet.data)
        print('\nПрограмма остановлена принудительно, данные сохранены')


if __name__ == '__main__':
    main()
