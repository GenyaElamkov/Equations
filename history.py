"""
Сохраняет в файл.
"""


def print_txt(array: list) -> None:
    """Выводим в txt"""
    with open('equation.txt', 'w', encoding='utf-8') as f:
        f.writelines('Уравнения:\n')
        for i in range(len(array)):
            f.writelines(f'{i + 1}) {array[i][0]}\n')

        f.writelines('\nОтветы:\n')
        for i in range(len(array)):
            f.writelines(f'{i + 1}) {array[i][1]}\n')


if __name__ == '__main__':
    arr = [['64 * (1x : 64) = 83', 'x = 83'],
           ['(76 + 6x) - 57 = 25', 'x = 1'],
           ['(49 + 5x + 23) = 97', 'x = 5'],
           ['(82 - 4x) * 2 = 76', 'x = 11'],
           ['23 + (3x - 91) = 73', 'x = 47']]

    print_txt(arr)
