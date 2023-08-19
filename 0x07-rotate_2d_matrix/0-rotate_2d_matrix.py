#!/usr/bin/python3
"""
This is technical interviw question to solve Rotate 2D Matri'x
"""


def rotate_2d_matrix(matrix):
    """
    This function rotats the 2D matrix 90 degree clockwise
    """
    copied_matrix  = matrix.copy()
    reverced_copy = copied_matrix[::-1]
    for elements in range(len(matrix[0])):
        new_matrix = []  
        # This is an array holds the value of the resultant marix
        for low in reverced_copy:
            new_matrix.append(row[elements])
            matrix[elements] = new_matrix
