from datetime import datetime, date


class OperationValidator:
    """
    Класс, предоставляющий методы для валидации пользовательского ввода операции.
    """
    @staticmethod
    def get_validated_amount() -> float:
        """
        Получает и возвращает корректно введенную пользователем сумму операции.
        :return: Введенная пользователем сумма операции.
        """
        while True:
            amount: str = input('Введите сумму: ')
            if amount.replace('.', '', 1).isdigit():
                return round(float(amount), 2)
            else:
                print('Сумма должна быть числом.')

    @staticmethod
    def get_validated_category() -> str:
        """
        Получает и возвращает корректно введенную пользователем категорию операции.
        :return: Введенная пользователем категория операции.
        """
        while True:
            category: str = input('Введите категорию (Доход/Расход): ').lower()
            categories: list[str] = ['доход', 'расход']
            if category in categories:
                return category
            else:
                print('Категория должна быть либо "Доход", либо "Расход".')

    @staticmethod
    def get_validated_date() -> str:
        """
        Получает и возвращает корректно введенную пользователем дату операции в формате строки.
        :return: Введенная пользователем дата операции в формате строки.
        """
        while True:
            search_date: str = input('Введите дату: ')
            try:
                validated_date: date = datetime.fromisoformat(search_date).date()
            except ValueError as e:
                print(e)
                print('Неверный формат даты!\nОжидаемый формат: 2024-05-03\n')
            else:
                return str(validated_date)

    @staticmethod
    def get_validated_search_key(categories: dict[str, str]) -> str:
        """
        Получает и возвращает корректно введенный пользователем ключ поиска операции.
        :param categories: Словарь категорий
        :return: Введенный пользователем ключ поиска операции.
        """
        while True:
            user_key: str = input('Выберите ключ для поиска (дата/категория/сумма): ').lower()
            search_key: str = categories.get(user_key)
            if search_key:
                return search_key
            print('Такого ключа нет')

    @staticmethod
    def get_validated_id_input() -> int:
        """
        Получает и возвращает корректно введенный пользователем идентификатор операции.
        :return: Введенный пользователем идентификатор операции.
        """
        while True:
            try:
                operation_id: int = int(input('Введите id записи для редактирования: '))
            except ValueError:
                print('Вы должны вводить число')
            else:
                return operation_id

    @staticmethod
    def get_validated_field_input() -> str:
        """
        Получает и возвращает корректно введенное пользователем поле для изменения операции.
        :return: Введенное пользователем поле для изменения операции.
        """
        fields: dict[str, str] = {
            'дата': 'date',
            'категория': 'category',
            'сумма': 'amount',
            'описание': 'description',
        }
        while True:
            print('Выберите поле для изменения(дата, категория, сумма, описание):')
            field: str = input().lower().strip()
            if field in fields:
                return fields.get(field)
            else:
                print('Такого поля нет!')

