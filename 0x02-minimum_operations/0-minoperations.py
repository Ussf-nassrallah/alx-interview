#!/usr/bin/python3
"""
minimum_operations: solution
"""


def minOperations(n):
    ''' minOperations(n) '''
    if n <= 1:
        return 0

    (idx, num, output) = (2, n, 0)
    while idx <= num:
        if num % idx == 0:
            output += idx
            num /= idx
        else:
            idx += 1
    return output
