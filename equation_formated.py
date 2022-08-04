"""
Форматирует строку уравнения для вывода на печать.
"""


def format_chars(line) -> str:
    """Форматирует строку уравнения"""
    line = _replace_chars(line)
    line = _removing_multiplier(line)
    return line


def _removing_multiplier(line: str) -> str:
    """Удалят знак * с формулы для печати."""
    array = line.split()
    for i in range(len(array)):
        if len(array[i]) > 1:
            array[i] = array[i].replace('*', '')
    return ' '.join(array)


def _replace_chars(line: str) -> str:
    """Меняет символ в уравнении на привычный нам вид."""
    return line.replace('/', ':')


if __name__ == '__main__':
    text = '(4 * 2*x * 13) = 39;x = 11'
    print(format_chars(text))

    text = '(3*x / 3*x / 4*x) = 44;x = 2'
    print(format_chars(text))
