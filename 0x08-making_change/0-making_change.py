#!/usr/bin/python3
"""
Making Change Module
"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    curTotal = 0
    minCoins = 0
    for coin in coins:
        bal = (total - curTotal)//coin
        curTotal += bal*coin
        minCoins += bal
        if curTotal == total:
            return minCoins
    return -1
