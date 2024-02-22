#!/usr/bin/python3
''' 0x07. Rotate 2D Matrix solution '''


def rotate_2d_matrix(matrix):
    ''' rotate_2d_matrix '''
    matrix_size = len(matrix)

    for idx in range(int(matrix_size / 2)):
        end = (matrix_size - idx - 1)
        for j in range(idx, end):
            start = (matrix_size - 1 - j)
            helper = matrix[idx][j]
            matrix[idx][j] = matrix[start][idx]
            matrix[start][idx] = matrix[end][start]
            matrix[end][start] = matrix[j][end]
            matrix[j][end] = helper
