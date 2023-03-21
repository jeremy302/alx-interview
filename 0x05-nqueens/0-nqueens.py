#!/usr/bin/python3
''' prints all solutions to the nquess problem '''
from sys import argv


def nqueens(n):
    ''' finds solutions to the nqueens problem '''
    i, buf = [0, [0 for _ in range(n)]]
    while buf[0] < n:
        if buf[i] >= n:
            i -= 1
        elif all(all((k-j) and (buf[k]-buf[j])/(k-j) not in [0, 1, -1]
                     for k in range(j)) for j in range(1, i + 1)):
            if i+1 >= n:
                yield [[ind, buf[ind]] for ind in range(n)]
                i -= 1
            else:
                i += 1
                buf[i] = 0
                continue
        buf[i] += 1
if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
        if n < 4:
            print('N must be at least 4')
            exit(1)
        for solution in nqueens(n):
            print(solution)
    except ValueError:
        print('N must be a number')
        exit(1)
