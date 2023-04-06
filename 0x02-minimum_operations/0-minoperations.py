#!/usr/bin/python3
''' minimum operations module '''
from functools import reduce


def minOperations(n):
    ''' gets minumim number of operations '''
    factors = sorted(set(
        reduce(list.__add__, ([i, n//i] for i in range(
            1, int(n**0.5) + 1) if n % i == 0))) if n > 0 else [])[1:]

    ops = 0
    n = 1
    for f in factors:
        if f % n == 0:
            ops += f // n
            n = f
    return ops
