#!/usr/bin/python3
''' rotate 2d matrix module '''


def array_cord(x, y, n):
    ''' gets the array coordinate given a cartesian coordinate  '''
    return (n - y - 1, x)

def cartesian_cord(i, j, n):
    ''' gets the cartesian coordinate given an array coordinate  '''
    return (j, n - i - 1)

def transform_rotate2d(i, j, n):
    ''' rotates an array coordinate by 90° '''
    cord = cartesian_cord(i, j, n)

    # multiplying by 90° clockwise transformation matrix (270° anticlockwise)
    tcord = [cord[1], -cord[0]]
    # translating to first quadrant
    tcord[1] = tcord[1] + n - 1

    return array_cord(*tcord, n)

def rotate_2d_matrix(matrix):
    ''' rotates a 2d matrix '''
    n = len(matrix)
    for i in range(0, n - 1):
        pos = (0, i)
        npos = transform_rotate2d(*pos, n)
        carry = matrix[0][i]
        while npos != (0, i):
            tmp = matrix[npos[0]][npos[1]]
            matrix[npos[0]][npos[1]] = carry # matrix[pos[0]][pos[1]]
            carry = tmp
            pos = npos
            npos = transform_rotate2d(*pos, n)
        matrix[0][i] = carry
    
