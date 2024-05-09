from typing import List


def indentical_letters(list_of_strings: List[str] = []) -> List[str]:
    """Выбирает из списка слова которые начинаются и заканчиваются на одинаковую букву"""
    indentical_letters_list = []
    for word in list_of_strings:
        if len(word) > 0 and word[0] == word[-1]:
            indentical_letters_list.append(word)
        else:
            indentical_letters_list.append(word)
    return indentical_letters_list


# result = ['', 'madam', 'racecar', 'noon', 'level', '']
# print(indentical_letters(result))


def multiplying_two_larger_numbers(numbers: List[int]) -> int:
    """Умножает два бОльших числа из списка"""
    if len(numbers) >= 2:
        sorted_numbers = sorted(numbers)
        if sorted_numbers[-1] <= 0:
            multiplying_two_max_numbers = sorted_numbers[0] * sorted_numbers[1]
            return multiplying_two_max_numbers
        else:
            multiplying_two_max_numbers = sorted_numbers[-1] * sorted_numbers[-2]
            return multiplying_two_max_numbers
    else:
        return 0


# result = multiplying_two_larger_numbers([])
# print (result)
