from equations import generate_equate
from equation_formated import format_chars
from progress import progress_bar
from history import save_txt

"""
Генератор линейных уравнений
"""


# def count_equate(number_equations: int, size: int, factor: int, summa: int) -> list:
#     """Возвращает кол-во уравнений."""
#     arr = []
#     for i in range(1, number_equations + 1):
#         text = generate_equate(size, factor, summa)
#         format_text = format_chars(text).split(';')
#         arr.append(format_text)
#         # progress_bar(i)
#
#     return arr

def main(size: int, factor: int, summa: int) -> list:
    """Возвращает кол-во уравнений."""
    text = generate_equate(size, factor, summa)
    return format_chars(text).split(';')


#
# def main():
#     print('-' * 50)
#     print('[Help:] Если ввести кол-во аргументов 1 - то добавится "деление"')
#     print('-' * 50)
#     try:
#         size = int(input('[1] Введите кол-во аргументов: '))  # Размер ур-я аргументов.
#         factor = int(input('[3] Введите множитель (10, 100, 1000): '))  # factor*X = summa.
#         summa = int(input('[2] Введите max сумму равенства: '))  # Равенство ур-я = 100.
#         number_equations = int(input('[4] Введите кол-во уравнений: '))  # Кол-во ур-й.
#     except ValueError:
#         print('Введите целые числа.')
#         exit(1)
#
#     arr = count_equate(number_equations, size, factor, summa)
#     print_txt(arr)
#
#     input('[!] Ваш файл создан, находится рядом с программой')


if __name__ == '__main__':
    # main()
    count_equate(size=1, factor=10, summa=100)
