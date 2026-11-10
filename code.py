"""Проверка порядка строчных букв в пяти массивах. Python 3.10+."""
from collections.abc import Sequence


def validate_array(elements: Sequence[str]) -> None:
    if len(elements) > 100:
        raise ValueError("Размер массива превышает 100 элементов")
    for item in elements:
        if (not isinstance(item, str) or len(item) != 1
                or not ("A" <= item <= "Z" or "a" <= item <= "z")):
            raise ValueError("Элементы массива должны быть латинскими буквами")


def check_array(*elements: str) -> bool:
    """Все элементы передаются как аргументы; равные буквы разрешены."""
    validate_array(elements)
    previous = None
    for letter in elements:
        if "a" <= letter <= "z":
            if previous is not None and letter < previous:
                return False
            previous = letter
    return True


def find_arrays(arrays: Sequence[Sequence[str]]) -> list[int]:
    if len(arrays) != 5:
        raise ValueError("Требуется ровно пять массивов")
    return [number for number, array in enumerate(arrays, start=1)
            if check_array(*array)]


def format_result(numbers: Sequence[int]) -> str:
    if not numbers:
        return "Нет массивов, удовлетворяющих условию"
    return "Номера массивов: " + ", ".join(map(str, numbers))


def parse_array(line: str) -> list[str]:
    """Допустимы abc и a b c; пустая строка задаёт пустой массив."""
    stripped = line.strip()
    return stripped.split() if any(c.isspace() for c in stripped) else list(stripped)


def main() -> int:
    try:
        arrays = [parse_array(input()) for _ in range(5)]
        print(format_result(find_arrays(arrays)))
    except (ValueError, EOFError) as error:
        message = "Недостаточно строк ввода" if isinstance(error, EOFError) else str(error)
        print("Ошибка: " + message)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
