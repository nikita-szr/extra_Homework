def sum_divisible_by_3_or_5(lst):
    """
    Функция принимает на вход список чисел и возвращает сумму всех элементов списка,
    которые делятся на 3 или 5 без остатка.
    """
    result = 0
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


def check_email(email):
    """Функция проверяет является ли переданное значение е-мейлом"""
    if "@" in email and "." in email:
        if email.index("@") > 0 and email[-1] != ".":
            return True
    return False


def count_number_in_list(numbers, number_to_count):
    """Считывает количество вхождений переданного числа в список."""
    count = 0
    for num in numbers:
        if num == number_to_count:
            count += 1
    return count


def calculate_area(shape, sides):
    if shape == "квадрат":
        return sides[0] ** 2
    elif shape == "прямоугольник":
        return sides[0] * sides[1]
    elif shape == "треугольник":
        a, b, c = sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    elif shape == "круг":
        return 3.14 * sides[0] ** 2
    else:
        return None
