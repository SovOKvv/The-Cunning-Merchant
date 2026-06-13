def print_menu():
    print('\n' + '='*35)
    print('           ХИТРЫЙ КУПЕЦ')
    print('='*35)
    print('1. Запустить расчет (ввод вручную)')
    print('2. Загрузить данные из файла input.txt')
    print('3. Показать справку по задаче')
    print('4. Выход')
    print('='*35)


def print_help():
    print('\n------------- СПРАВКА -------------')
    print('Два купца везут по N одинаковых тюков товара (всего 2*N).')
    print('В шторм капитан решает выбросить половину груза (N тюков) по кругу.')
    print('Отсчет начинается с позиции M по часовой стрелке.')
    print('Выбрасывается каждый (K + 1)-й тюк.')
    print('-' * 35)


def get_safe_int_input(number, min_value=0, max_value=None):
    while True:
        try:
            user_input = input(number).strip()
            if not user_input:
                print('Ошибка: ввод не может быть пустым.')
                continue
            value = int(user_input)

            if value < min_value:
                print(f'Ошибка: число должно быть не меньше {min_value}.')
                continue

            if max_value is not None and value > max_value:
                print(f'Ошибка: число должно быть не больше {max_value}.')
                continue

            return value
        except ValueError:
            print('Ошибка: введите корректное целое число.')


def show_results(task, safe_places):
    print('\n' + '-'*35)
    print('             РЕЗУЛЬТАТЫ')
    print('-'*35)
    print(f'Количество тюков одного купца (N): {task.n}')
    print(f'Всего мест вдоль бортов (2*N):     {task.total_bales}')
    print(f'Стартовое число месяца (M):        {task.m}')
    print(f'Шаг пропуска тюков (K):            {task.k}')
    print('-'*35)
    print(f'Безопасные позиции для первого купца:')
    print(' '.join(str(place) for place in safe_places))
    print('-'*35)