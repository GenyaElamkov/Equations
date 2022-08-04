from random import randint, choice, randrange


def generate_equate(equation_size: int, multiplier_size: int, sum_equality: int) -> str:
    """Возвращает сгенерированная уравнение."""
    max_size = sum_equality  # Максимальный размер множителя на "х"
    sign = ('+', '-', '*', '/')
    sum_equality = randint(1, sum_equality)

    while True:
        # Генерируем уравнения.
        line = ''
        for _ in range(equation_size):
            if equation_size == 1:
                line = f'{randint(1, max_size)} {choice(sign)} {randint(1, multiplier_size)}*x {choice(sign)} ' \
                       f'{randint(1, max_size)}'
                break
            else:
                line += f'{randint(1, multiplier_size)}*x {choice(sign[:-1])} '

        line = line.rstrip()
        if line[-1] in sign:
            line = line[:-1]

        # Генератор скобок.
        line = _generate_bracket(line)

        # Проверка на равенство уравнения.
        for x in range(1, max_size):
            # x - используется в eval() для расчета.
            try:
                if eval(line) == sum_equality:
                    return f'{line} = {sum_equality};x = {x}'

            except ZeroDivisionError:
                break


def _generate_bracket(text: str) -> str:
    """Генератор скобок."""
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


if __name__ == '__main__':
    size = 1
    factor = 10
    summa = 100
    print(generate_equate(size, factor, summa))

    size = 3
    factor = 10
    summa = 100
    print(generate_equate(size, factor, summa))
