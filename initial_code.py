"""Первоначальная учебная версия для инспекции. Содержит дефекты."""


def check_array(array):
    letters = [item for item in array if item.islower()]
    return letters == sorted(set(letters))


def find_arrays(arrays):
    return [i for i, array in enumerate(arrays) if check_array(array)]
