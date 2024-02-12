from constants import PATH
from csv_crud import ActionFile
from exceptions import NotFound
from terminal import Terminal
from utils import create_file, create_table, paginator, remove_spaces

terminal = Terminal()
csv = ActionFile(PATH)


def write() -> None:
    """Запись новых данных в справочник."""
    try:
        data = terminal.get_data().split(',')
        remove_spaces(data)
        assert len(data) == 6, 'Неполные данные'
        csv.write(data)
        terminal.added_data()
    except (AssertionError, ValueError) as error:
        terminal.error_input()
        terminal.print_error(error)


def read() -> None:
    """Чтение записей из справочника."""
    data = csv.read()
    paginator(data)


def update() -> None:
    """Обновление записей справочника."""
    try:
        number = terminal.get_number()
        data = terminal.get_data().split(',')
        remove_spaces(data)
        new_row = csv.update(number, data)
        create_table(new_row)
    except KeyError as error:
        terminal.error_input()
        terminal.print_error(error)
    except NotFound:
        terminal.not_found_entry()


def search() -> None:
    """Поиск записей по справочнику."""
    data = terminal.get_data().split(',')
    remove_spaces(data)
    result = csv.serach(data)
    create_table(result)


def start_terminal() -> None:
    """Запускает обработку команд."""
    terminal.start()
    while True:
        command = terminal.get_command()
        if command == terminal.exit:
            break
        try:
            commands[command]()
        except KeyError:
            terminal.not_found_command()


@create_file
def main() -> None:
    """Запускает работу терминала."""
    start_terminal()


commands = {
    'write': write,
    'read': read,
    'update': update,
    'search': search,
    'help': terminal.helper,
}


if __name__ == '__main__':
    main()
