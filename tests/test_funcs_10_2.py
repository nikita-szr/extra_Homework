import pytest

from src.funcs_10_2 import (
    calculate_area,
    check_email,
    count_number_in_list,
    sum_divisible_by_3_or_5,
)


@pytest.fixture
def testing_func_1():
    return [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [1, 2, 4, 7, 8]]


def test_sum_divisible_by_3_or_5_general_case(testing_func_1):
    assert sum_divisible_by_3_or_5(testing_func_1[0]) == 3 + 5 + 6 + 9 + 10
    assert sum_divisible_by_3_or_5(testing_func_1[1]) == 0
    assert sum_divisible_by_3_or_5(testing_func_1[2]) == 0


@pytest.mark.parametrize(
    "email, exception",
    [
        ("primer@mail.com", True),
        ("primer.mail@mail.com", True),
        ("primeremail.com", False),
        ("@mail.com", False),
        ("primer@mail.", False),
        ("", False),
    ],
)
def test_check_email(email, exception):
    assert check_email(email) == exception


@pytest.fixture
def test_count_number_in_list():
    return [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [1, 5, 6]]


def testing_count_number_in_list(test_count_number_in_list):
    assert (
        count_number_in_list(
            test_count_number_in_list[0], test_count_number_in_list[1][0]
        )
        == 2
    )
    assert (
        count_number_in_list(
            test_count_number_in_list[0], test_count_number_in_list[1][1]
        )
        == 2
    )
    assert (
        count_number_in_list(
            test_count_number_in_list[0], test_count_number_in_list[1][2]
        )
        == 0
    )


@pytest.mark.parametrize(
    "shape, sides, square",
    [
        ("квадрат", [4], 16),
        ("прямоугольник", [3, 5], 15),
        ("треугольник", [3, 4, 5], 6),
        ("круг", [2], 3.14 * 2**2),
    ],
)
def test_calculate_area(shape, sides, square):
    assert calculate_area(shape, sides) == square
