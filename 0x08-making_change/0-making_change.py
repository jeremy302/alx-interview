#!/usr/bin/python3
''' making change module '''

def makeChange(coins, total):
    ''''''
    coins = sorted(coins, reverse=True)
    n = 0
    i = 0
    while i < len(coins) and total > 0:
        coin = coins[i]
        if total - coin >= 0:
            total -= coin
            n += 1
        else:
            i += 1
    return n if i < len(coins) else -1
        
