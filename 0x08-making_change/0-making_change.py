#!/usr/bin/python3
"""Get the fewest number of coins to meet a given amount."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
        coins (list of int): The values of the coins in your possession.
        total (int): The total amount to achieve with the coins.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins, return -1.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    num_coins = 0
    sorted_coins = sorted(coins, reverse=True)

    for coin in sorted_coins:
        while total >= coin:
            total -= coin
            num_coins += 1
        if total == 0:
            return num_coins
    return -1
