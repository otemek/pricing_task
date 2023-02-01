def max_result(prices: list) -> int:
    """Gets the highest income from the prices, sorted by transaction date

    Args:
        prices (list): prices, sorted by transaction date

    Returns:
        list: biggest difference between prices 
    """
    max_diff = 0
    for idx in range(len(prices)-1, 0, -1):
        for iidx in reversed(range(idx)):    
            calculated_value = prices[idx] - prices[iidx]
            if calculated_value > max_diff:
                max_diff = calculated_value
    return max_diff



# print(max_result([10, 20, 30, 5]))
# print(max_result([20, 40, 10, 20, 50]))
# print(max_result([50, 40, 30, 10, 20]))
# print(max_result([50, 40, 30, 20, 10]))
# print(max_result([10, 20, 30, 5, 40, 50]))
# print(max_result([2, 3, 4, 5, 6, 1, 2, 3, 9]))