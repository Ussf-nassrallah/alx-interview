#!/usr/bin/env python3
'''Change comes from within - problem solution'''


def makeChange(coins, total):
    ''' makeChange method '''
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    num_coins = 0
    sorted_coins = sorted(coins)[::-1]

    for coin in sorted_coins:
        while coin <= total:
            total -= coin
            num_coins += 1
        if total == 0:
            return num_coins

    return -1
