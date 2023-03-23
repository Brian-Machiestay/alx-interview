#!/usr/bin/python3
"""return the fewest number of coins denominations for total"""


def makeChange(coins, total):
    """return fewest number of coins denominations"""
    allcoins = coins.copy()
    allcoins.sort()
    allcoins.reverse()
    left = total
    minCoins = 0

    for coin in allcoins:
        if coin <= left and left % coin == 0:
            minCoins = minCoins + left // coin
            left = 0
        elif coin <= left:
            leftbefore = left
            left = left - ((left // coin) * coin)
            minCoins = minCoins + (leftbefore // coin)
        if left == 0:
            return minCoins
    return -1
