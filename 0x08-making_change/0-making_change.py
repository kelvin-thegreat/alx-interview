#!/usr/bin/python3
"""Module for making change using the fewest number of coins"""

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

    """Initialize a table to store the minimum number of coins for each amount"""
    dp = [float('inf')] * (total + 1)
    """Base case: 0 coins needed to make change for amount 0"""
    dp[0] = 0
    """Iterate through each coin value"""
    for coin in coins:
        """Update the table for each possible amount"""
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    """If dp[total] is still infinity, it means the total cannot be achieved"""
    return dp[total] if dp[total] != float('inf') else -1
