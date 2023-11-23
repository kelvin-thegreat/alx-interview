#!/usr/bin/python3
"""
Change-making
"""


def make_change(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    Args:
        coins (list): List of coin values.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0
    remaining = total, coinsCount = 0, coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remaining > 0:
        if coin_index >= n:
            return -1
        if remaining - sorted_coins[coin_index] >= 0:
            remaining -= sorted_coins[coin_index]
            coinsCount += 1
        else:
            coin_idx += 1
    return coinsCount
