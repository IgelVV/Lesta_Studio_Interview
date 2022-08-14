from random import randint
from timeit import repeat


ARRAY_LENGTH = 1000


def run_sorting_algorithm(algorithm, array):
    """
    Функция для оценки времени выполнения алгоритма
    """
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. \n\tMinimum execution time: {min(times)}")


#  Для малых массивов выполняется достаточно быстро, наилучший сценарий при
#  сортировке уже отсортированного массива.
def insertion_sort(array, left=0, right=None):
    """
    Сортировка вставкой
    :param array: Массив чисел
    :param left: Начало диапазона сортировки
    :param right: Конец диапазона сортировки
    :return: Отсортированный массив
    """
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]

        j = i - 1

        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


def merge(left, right):
    """
    Функция слияния двух отсортированных массивов.
    :param left: первый массив.
    :param right: Второй массив.
    :return: Итоговый массив массив.
    """

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


#  Использует преимущества сортировки вставкой на малых массивах и при работе
#  на уже отсортированных данных, но при этом масштабирует эффект,
#  разбивая основной массив на малые части.
def timsort(array, min_run=32):
    """
    Упрощенная сортировка timsort.
    :param array: Массив чисел.
    :param min_run: Размер небольших порций массива от 32 до 64 для быстрой
    сортировки вставкой.
    :return: Отсортированный массив.
    """
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1]
            )

            array[start:start + len(merged_array)] = merged_array
        size *= 2

    return array


def merge_sort(array):
    """
    Сортировка слиянием
    :param array:
    :return:
    """
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


if __name__ == "__main__":
    #  timsort показывает лучшие результат из трех написанных алгоритмов.
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="timsort", array=array)

    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="insertion_sort", array=array)

    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="merge_sort", array=array)

    #  Встроенная функция sorted() часто является лучшим решением.
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="sorted", array=array)
