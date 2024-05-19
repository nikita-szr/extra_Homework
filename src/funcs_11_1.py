def non_empty_truths(input_list):
    return [[i for i in list if i and i != []]for list in input_list if list]


# print(non_empty_truths([]))  # []
# print(non_empty_truths([[], []]))  # []
# print(non_empty_truths([[0]]))  # []
# print(non_empty_truths([[0, ""], [False, None]]))  # []
# print(non_empty_truths([[0, 1, 2], [], [], [False, True, 42]]))  # [[1, 2], [True, 42]]


def my_map(f, xs):
    """Упрощенная версия map"""
    for x in xs:
        yield f(x)


def my_filter(f, xs):
    """Упрощенная версия filter"""
    for x in xs:
        if f(x):
            yield x


def replicate_each(n, xs):
    """Для каждого элемента итератора xs выдает на выход по n копий этого элемента"""
    pass


print(list(my_map(lambda x: x + 2, [-1, 2, -3])))  # [1, 4, -1]
print(list(my_filter(lambda x: x % 2 == 1, range(10))))  # [1, 3, 5, 7, 9]
