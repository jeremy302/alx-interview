#!/usr/bin/python3
''' minimum operations module '''


def minOperations(n):
    ''' gets minumim number of operations '''
    factors = [v for v in range(2, n + 1) if n % v == 0]
    ops = 0
    n = 1
    for f in factors:
        if f % n == 0:
            ops += f // n
            n = f
    return ops
