#!/usr/bin/python3
''' prime game module '''


def playMatch(n):
    ''' plays a single round '''
    nums = list(range(2, n+1))
    winner = 1
    while nums:
        pick = nums[0]
        nums = [v for v in nums if v % pick]
        winner = 1 - winner
    return winner


def isWinner(x, nums):
    ''' plays a full game '''
    if type(x) is not int or x < 1:
        return None
    players = {0: 'Maria', 1: 'Ben'}
    wins = {0: 0, 1: 0}
    for num in nums:
        wins[playMatch(num)] += 1
    return (None if wins[0] == wins[1]
            else players[0] if wins[0] > wins[1]
            else players[1])
