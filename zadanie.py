def max_result(prices: list) -> int:
    """Gets the highest income from the prices, sorted by transaction date
        with assumption that we can't buy in the future
    Args:
        prices (list): prices, sorted by transaction date

    Returns:
        list: biggest difference between prices
    """
    max_diff = 0
    for idx in reversed(range(len(prices))):
        for iidx in reversed(range(idx)):
            calculated_value = prices[idx] - prices[iidx]
            if calculated_value > max_diff:
                max_diff = calculated_value
    return max_diff
