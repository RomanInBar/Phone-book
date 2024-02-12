import csv
import fileinput

from exceptions import NotFound


class ActionFile:
    """path - path to file."""

    def __init__(self, path: str) -> None:
        self.file = path

    def write(self, data: list[str]):
        """Записывает данные в файл."""
        with open(self.file, mode='a', encoding='utf8') as file:
            w = csv.writer(file, delimiter=',')
            w.writerow(data)

    def read(self) -> list[list]:
        """Возвращает все данные из файла."""
        with open(self.file, mode='r', encoding='utf8') as file:
            data = [row for row in csv.reader(file, delimiter=',')]
            return data[1:]

    def update(self, index: str, data: list[str]) -> list[list]:
        """Обновляет данные в файле."""
        with fileinput.input(
            files=(self.file), inplace=True, mode='r', encoding='utf8'
        ) as file:
            reader = csv.DictReader(file)
            result = None
            print(",".join(reader.fieldnames))
            for row in reader:
                if row['Личный телефон'] == index:
                    for item in data:
                        key, value = item.split(' ')
                        row[key] = value
                        result = row.values()
                print(','.join(row.values()))
            if result:
                return [result]
            raise NotFound

    def serach(self, data: list[str]) -> list[list]:
        """Поиск данных в файле."""
        with open(self.file, mode='r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            result = [
                row.values()
                for row in reader
                if set(row.values()) & set(data) == set(data)
            ]
            return result
