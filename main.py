from random import randint, choice
from tqdm import tqdm
from time import sleep

"""
Генератор линейных уравнений
"""


def generate_equate(size, factor, summa):
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

        # Проверка на равенство уравнения.
        for x in range(1, max_size):
            # x - используется в eval() для расчета
            if int(eval(line)) == summa:
                res = f'{line} = {summa};x = {x}'
                return res


def progress_bar(counter):
    for _ in tqdm(range(counter), ncols=80, ascii=True, desc='Total'):
        sleep(0.1)


def count_equate(number_equations, size, factor, summa,):
    arr = []
    for i in range(1, number_equations + 1):
        arr.append(generate_equate(size, factor, summa).split(';'))
        progress_bar(i)
    return arr


def replace_chars(arr):
    """
    Меняет символ в уравнении на привычный нам вид.
    [!] Пока не используется.
    :param arr: list
    :return: list
    """
    for line in arr:
        line[0] = ''.join(line[0]).replace('/', ':')
    return arr


def print_equate(arr):
    with open('equation.txt', 'w', encoding='utf-8') as f:
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
    print_equate(replace_chars(arr))
    input('[!] Ваш файл создан, находится рядом с программой')


if __name__ == '__main__':
    main()
