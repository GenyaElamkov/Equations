from random import randint, choice
from tqdm import tqdm
from time import sleep

"""
Генератор линейных уравнений
"""


def progress_bar(counter):
    for _ in tqdm(range(counter), ncols=80, ascii=True, desc='Total'):
        sleep(0.1)


def generate_equate(size, factor, summa, number_equations):
    """
    Генерирует линейное уравнение.
    :param factor:
    :param size: int.
    :param summa: int.
    :param number_equations: int.
    :return: list.
    """
    max_size = summa  # Максимальный размер множителя на "х"
    sign = ('+', '-', '*',)
    resoult = []
    counter = 0
    while counter < number_equations:
        summa = randint(1, summa)
        flag = False
        line = ''
        while not flag:
            # Генерируем уравнения.
            for _ in range(size):
                equate = f'{randint(1, factor)}*x {choice(sign)} '
                line += equate

            line = line[:-2].rstrip()

            # Проверка на равенство уравнения.
            for x in range(1, max_size):
                # x - используется в eval() для расчета
                if int(eval(line)) == summa:
                    res = f'{line} = {summa};x = {x}'
                    resoult.append(res.split(';'))
                    flag = True
                    break

            if flag:
                counter += 1
                progress_bar(counter)
                break
            else:
                line = ''

    return resoult


def replace_chars(arr):
    """
    Меняет символ в уравнении на привычный нам вид.
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
    arr = generate_equate(size, factor, summa, number_equations)
    print_equate(replace_chars(arr))


if __name__ == '__main__':
    main()
