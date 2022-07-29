from random import randint, choice
"""
Генератор линейных уравнений
"""


def generate_equate(size, summa, number_equations):
    """
    Генерирует линейное уравнение.
    :param size: int.
    :param summa: int.
    :param number_equations: int.
    :return: list.
    """
    max_size = summa  # Максимальный размер множителя на "х"
    sign = ('+', '-', '*', '/',)
    resoult = []
    counter = 0
    while counter < number_equations:
        summa = randint(1, summa)
        flag = False
        line = ''
        while not flag:
            # Генерируем уравнения.
            for _ in range(size):
                # x - используется в eval() для расчета
                equate = f'{randint(1, max_size)}*x {choice(sign)} '
                line += equate

            line = line[:-2].rstrip()

            # Проверка на равенство уравнения.
            for x in range(1, max_size):
                if int(eval(line)) == summa:
                    res = f'{line} = {summa};x = {x}'
                    flag = True
                    break

            if flag:
                resoult.append(res.split(';'))
                counter += 1
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
            f.writelines(f'{i+1}) {arr[i][0]}\n')

        f.writelines('\nОтветы:\n')
        for i in range(len(arr)):
            f.writelines(f'{i+1}) {arr[i][1]} ')


def main():
    size = int(input('Введите кол-во аргументов: '))  # Размер ур-я аргументов.
    summa = int(input('Введите max сумму равенства: '))  # Равенство ур-я = 100.
    number_equations = int(input('Введите кол-во уравнений: '))  # Кол-во ур-й.
    arr = generate_equate(size, summa, number_equations)
    print_equate(replace_chars(arr))


if __name__ == '__main__':
    main()
