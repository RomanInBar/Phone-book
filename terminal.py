class Terminal:
    def __init__(self) -> None:
        self.exit = 'stop'

    def start(self) -> None:
        print(
            'Добро пожаловать в телефонный справочник.\n'
            'Для получения информации, введите команду help'
        )

    def get_data(self) -> str:
        data = input('Введите данные: ')
        return data.title()

    def get_command(self) -> str:
        command = input('Введите команду: ')
        return command

    def get_number(self):
        number = input('Введите личный телефон: ')
        return number

    def not_found_command(self) -> None:
        print('Команда не распознана.')

    def not_found_entry(self):
        print('Запись не найдена.')

    def added_data(self):
        print('Данные добавлены.')

    def error_input(self):
        print('Ошибка ввода данных.')

    def print_error(self, error):
        print(error)

    def helper(self):
        print(
            'Команды для использования функционала приложения.\n\n'
            'write          Добавить новую запись в файл. Данные '
            'вводятся поочередно, через запятую:\n'
            '               Фамилия,Имя,Отчество,Название орагнизации,'
            'Рабочий телефон,Личный телефон.\n\n'
            'read           Получить данные из справочника.\n\n'
            'update         Обновить данные записи. Для этого, '
            'сначала введите личный телефон абонента,\n'
            '               после вводите данные, которые хотите '
            'изменить, в формате: Имя Иван,Фамилия Иванов.\n\n'
            'search         Поиск записи в файле. Для этого введите '
            'характеристики поиска (Имя/фамилию/телефон).\n'
            '               Можно использовать одно или несколько значений.\n'
            '               Пример: Иванов,Иван,9999999\n\n'
            f'{self.exit}           Завершение работы.\n\n'
        )
