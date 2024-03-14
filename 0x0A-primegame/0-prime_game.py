#!/usr/bin/python3
""" prime_game """


def isWinner(x, nums):
    ''' isWinner method '''
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    result = [1 for x in range(sorted(nums)[-1] + 1)]
    result[0], result[1] = 0, 0

    for index in range(2, len(result)):
        helper(result, index)

    for num in nums:
        if sum(result[0:num + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def helper(ls, x):
    ''' helper '''
    for index in range(2, len(ls)):
        try:
            ls[index * x] = 0
        except (ValueError, IndexError):
            break
