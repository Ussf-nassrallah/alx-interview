#!/usr/bin/python3
''' 0. Log parsing: solution '''

import sys


def helper(codes, size):
    '''helper function'''
    print("File size: {}".format(size))
    sorted_codes = sorted(codes.items())

    for key, value in sorted_codes:
        if value is not 0:
            print(f"{key}: {value}")


if __name__ == "__main__":
    codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    size = 0
    counter = 0

    try:
        for result in sys.stdin:
            counter += 1
            info = result.split()
            try:
                size += int(info[-1])
            except:
                pass
            try:
                codes[info[-2]] += 1
            except:
                pass
            if counter % 10 is 0:
                helper(codes, size)
        helper(codes, size)
    except KeyboardInterrupt:
        helper(codes, size)
        raise
