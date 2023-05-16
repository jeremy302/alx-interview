#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

def test(mat):
    print_matrix(mat)
    rotate_2d_matrix(mat)
    print()
    print_matrix(mat)
    print('='*30 + '\n')

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j]).rjust(3), end=" ")
        print()

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    test(matrix)
    test([[1, 11, 13, 19], [41, 32, 6, 22], [55, 21, 41, 66], [77, 29, 78, 2]])
    test([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
    test([[5, 6], [7, 8]])
    test([[5, 8, 11, 14, 17, 20], [23, 26, 29, 32, 35, 38], [41, 44, 47, 50, 53, 56], [59, 62, 65, 68, 71, 74], [77, 80, 83, 86, 89, 92], [95, 98, 101, 104, 107, 110]])
