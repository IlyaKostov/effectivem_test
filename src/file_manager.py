import json
import os


class FileManager:
    """
    Класс для работы с файлами
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def load_data(self) -> list[dict[str, str]]:
        """
        Загружает данные из файла.
        :return: Возвращает список словарей с данными.
        """
        data: list = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError as e:
                    print(e.msg)
        return data

    def save_data(self, data: list[dict[str, str]]) -> None:
        """
        Сохраняет данные в файл.
        :param data: Список словарей с данными для сохранения.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
