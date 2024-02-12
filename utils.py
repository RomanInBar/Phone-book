import os

from tabulate import tabulate

from constants import HEADERS, PATH
from csv_crud import ActionFile
from terminal import Terminal

terminal = Terminal()


def create_table(data: list[list]):
    """Создаёт таблицу с данными в терминале."""
    headers = HEADERS
    print(tabulate(data, headers=headers))


def remove_spaces(string: list[str]) -> str:
    """Удаляет пробелы в начале и в конце строки."""
    for index in range(len(string)):
        string[index] = string[index].lstrip().rstrip()
    return string


def create_file(func):
    """
    Проверяет наличие рабочего файла.
    При отсутствии оного, создаёт его.
    """

    def wrapper(*args, **kwargs):
        try:
            assert os.path.exists(PATH)
            result = func(*args, **kwargs)
        except AssertionError:
            ActionFile(PATH).write(HEADERS)
            result = func(*args, **kwargs)
        return result

    return wrapper


def paginator(data: list[list], items_on_page: int = 5) -> None:
    """Функция для постраничного вывода информации."""
    start = 0
    page = 0
    end = items_on_page
    total = len(data)
    while True:
        create_table(data[start:end])
        print(
            f'\nСтраница: {page}, <- 1, 2 ->, '
            'x - вернуться к выбору действия.\n'
        )
        action = terminal.get_command()
        if action == '1' and page > 0:
            start -= items_on_page
            end -= (
                end % items_on_page if (end % items_on_page) else items_on_page
            )
            page -= 1
        elif action == '2' and total != end:
            start += items_on_page
            end = end + items_on_page if end + items_on_page < total else total
            page += 1
        elif action == 'x':
            break
        else:
            terminal.error_input()
            terminal.not_found_command()
    return
