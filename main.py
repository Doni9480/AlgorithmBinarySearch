"""
Бинарный поиск
"""
import time


def normal_search(search_list, num_x):
    """
    Реализация линейного поиска
    :param search_list:
    :param num_x:
    :return:
    """
    step = 0
    for n in search_list:
        if n == num_x:
            return step
        step += 1
    return None


# Бинарный поиск v1
# def search_binary(search_list, num_x):
#     step = 0
#     while True:
#         step += 1
#         midd = search_list[round(len(search_list) / 2)]
#         if midd == num_x:
#             return step
#         elif midd < num_x:
#             search_list = search_list[round(len(search_list) / 2):]
#         elif midd > num_x:
#             search_list = search_list[:round(len(search_list) / 2)]


def search_binary(list_search: list, item: int):
    """
    Реализация бинарного поиска  (правильный)
    :param list_search:
    :param item:
    :return:
    """
    low = 0
    high = len(list_search) - 1
    step = 0
    while low <= high:
        midd = round((low + high) / 2)
        midd_val = list_search[midd]
        step += 1
        if midd_val == item:
            return step
        elif midd_val > item:
            high = midd
        elif midd_val < item:
            low = midd
    return None


def main():
    search_list = list(range(100_000_000))
    n_x = 25_500_000
    start = time.process_time()
    n = normal_search(search_list, n_x)
    stop = time.process_time()
    start2 = time.process_time()
    b = search_binary(search_list, n_x)
    stop2 = time.process_time()
    print(f'normal: {n}, time: {stop - start}')
    print(f'binary: {b}, time: {stop2 - start2}')


if __name__ == '__main__':
    main()
