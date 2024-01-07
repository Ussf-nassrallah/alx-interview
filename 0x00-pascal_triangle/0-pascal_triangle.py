#!/usr/bin/python3

"""
-> Create a function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n:
-> Returns an empty list if n <= 0
->You can assume n will be always an integer
"""


def pascal_triangle(n):
    """ pascal_triangle """
    if n <= 0:
        return []

    output = []

    for idx in range(n):
        r = [1] * (idx + 1)
        for j in range(1, len(r) - 1):
            r[j] = output[idx - 1][j - 1] + output[idx - 1][j]
        output.append(r)

    return output
