import pytest

from zadanie import max_result


@pytest.mark.parametrize(
    ["prices", "expected"],
    [
        [[10, 20, 30, 40, 50, 60], 50],
        [[10, 20, 30, 5], 20],
        [[20, 40, 10, 20, 50], 40],
        [[50, 40, 30, 10, 20], 10],
        [[50, 40, 30, 20, 10], 0],
        [[50, 40, 30, 20, 10, 11], 1],
        [[10, 20, 30, 5, 40, 50], 45],
        [[2, 3, 4, 5, 6, 1, 2, 3, 9], 8],
    ],
)
def test_calculate_max_profit(prices: list, expected: int):
    actual = max_result(prices)
    assert actual == expected
