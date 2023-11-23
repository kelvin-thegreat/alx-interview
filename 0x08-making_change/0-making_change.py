#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
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

    remaining_amount = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining_amount > 0:
        if coin_index >= num_coins:
            return -1

        if remaining_amount - sorted_coins[coin_index] >= 0:
            remaining_amount -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1

    return coins_count
