import ui
from merchant import MerchantTask

FILE_NAME = 'input.txt'


def execute_and_show(n, m, k):
    print('\nВыполняется расчет...')
    task = MerchantTask(n, m, k)
    safe_places = task.find_safe_positions()
    ui.show_results(task, safe_places)


def process_file():
    print(f'\n--- Загрузка данных из файла {FILE_NAME} ---')

    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            content = f.read().split()

        if len(content) < 3:
            print(f'Ошибка: В файле {FILE_NAME} должно быть не менее 3 чисел (N, M, K).')
            return

        n_bales = int(content[0])
        month = int(content[1])
        k_interval = int(content[2])

        if n_bales < 1 or not (1 <= month <= 31) or k_interval < 0:
            print('Ошибка в файле: Некорректные параметры (N>=1, M должно быть от 1 до 31, K>=0).')
            return

        print(f'Данные успешно считаны: N={n_bales}, M={month}, K={k_interval}')
        execute_and_show(n_bales, month, k_interval)

    except FileNotFoundError:
        print(f'Ошибка: Файл "{FILE_NAME}" не найден в папке с программой.')
        print(f'Пожалуйста, создайте файл "{FILE_NAME}" и запишите туда три числа через пробел.')
    except ValueError:
        print(f'Ошибка: Содержимое файла {FILE_NAME} не является целыми цифрами.')


def main():
    while True:
        ui.print_menu()
        choice = ui.get_safe_int_input('Выберите пункт меню (1-4): ', min_value=1)

        if choice == 1:
            print('\n--- Ввод исходных данных вручную ---')
            n = ui.get_safe_int_input('Введите количество тюков N (>=1): ', min_value=1)
            m = ui.get_safe_int_input('Введите стартовую позицию M (день месяца): ', min_value=1, max_value=31)
            k = ui.get_safe_int_input('Введите шаг пропуска K (>=0): ', min_value=0)
            execute_and_show(n, m, k)

        elif choice == 2:
            process_file()

        elif choice == 3:
            ui.print_help()
            input('Нажмите Enter, чтобы вернуться в меню...')

        elif choice == 4:
            print('\nПрограмма завершена. Удачной торговли купцам!')
            break

        else:
            print('Ошибка: Такого пункта меню не существует.')


if __name__ == '__main__':
    main()