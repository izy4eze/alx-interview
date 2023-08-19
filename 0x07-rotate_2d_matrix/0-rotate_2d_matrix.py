#!/usr/bin/python3
"""
This is technical interviw question to solve Rotate 2D Matri'x
"""


def rotate_2d_matrix(matrix):
    """The function rotate_2d_matrix rotates two dimension matrix to 90 degree clockwise
    Args:
        matrix (list[[list]]): a matrix

    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            X = (n - i - j):
                # This is the current nummber
                tmp = matrix[i][j]
                # shift top to life move
                matrix[i][j] = matrix[x][i]
                # shift left to bottom move
                matrix[x][i] = matrix[y][x]
                # shift bottom to right
                matrix[y][x] = matrix[j][y]
                # finally shift right to top
                matrix[j][y] = tmp
