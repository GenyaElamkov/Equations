from random import randint, choice, randrange
from time import sleep

from tqdm import tqdm

"""
Генератор линейных уравнений
"""


def generate_bracket(text) -> str:
    """Генератор скобок"""
    arr = text.split()

    start = randrange(0, len(arr) - 1, 2)
    end = randrange(start, len(arr) - 1, 2)
    if start == end and start == 0:
        end = randrange(start + 2, len(arr), 2)
    elif start == end and end == len(arr) - 1:
        start = randrange(0, end - 1, 2)
    elif start == end and start >= 1:
        start = randrange(0, start + 1, 2)
        end = randrange(start + 2, len(arr), 2)

    arr[start] = '(' + arr[start]
    arr[end] = arr[end] + ')'

    return ' '.join(arr)


def generate_equate(size, factor, summa) -> str:
    """Возвращает сгенерированная уравнение."""
    max_size = summa  # Максимальный размер множителя на "х"
    sign = ('+', '-', '*',)
    summa = randint(1, summa)

    while True:
        # Генерируем уравнения.
        line = ''
        for _ in range(size):
            equate = f'{randint(1, factor)}*x {choice(sign)} '
            line += equate

        line = line[:-2].rstrip()

        # Генератор скобок.
        line = generate_bracket(line)

        # Проверка на равенство уравнения.
        for x in range(1, max_size):
            # x - используется в eval() для расчета.
            if int(eval(line)) == summa:
                res = f'{line} = {summa};x = {x}'
                return res


def progress_bar(counter):
    for _ in tqdm(range(counter), ncols=80, ascii=True, desc='Total'):
        sleep(0.1)


def removing_multiplier(text) -> str:
    """Удалят знак * с формулы для печати"""
    text = text.split()
    for i in range(len(text)):
        if len(text[i]) > 1:
            text[i] = text[i].replace('*', '')
    return ' '.join(text)


def count_equate(number_equations, size, factor, summa, ) -> list:
    """Возвращает кол-во уравнений."""
    arr = []
    for i in range(1, number_equations + 1):
        text = generate_equate(size, factor, summa)
        arr.append(removing_multiplier(text).split(';'))
        progress_bar(i)
    return arr


def print_equate(arr):
    with open('equation.txt', 'w', encoding='utf-8') as f:
        f.writelines('Уравнения:\n')
        for i in range(len(arr)):
            f.writelines(f'{i + 1}) {arr[i][0]}\n')

        f.writelines('\nОтветы:\n')
        for i in range(len(arr)):
            f.writelines(f'{i + 1}) {arr[i][1]} ')


def main():
    size = int(input('[1] Введите кол-во аргументов: '))  # Размер ур-я аргументов.
    factor = int(input('[3] Введите множитель (10, 100, 1000): '))  # factor*X = summa.
    summa = int(input('[2] Введите max сумму равенства: '))  # Равенство ур-я = 100.
    number_equations = int(input('[4] Введите кол-во уравнений: '))  # Кол-во ур-й.
    arr = count_equate(number_equations, size, factor, summa)
    print_equate(arr)
    input('[!] Ваш файл создан, находится рядом с программой')


if __name__ == '__main__':
    main()
