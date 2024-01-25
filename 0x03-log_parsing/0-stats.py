#!/usr/bin/python3
''' 0. Log parsing: solution '''


import re
from sys import stdin


def helper(inp):
    '''checker
    '''
    checks = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    valid = re.match(checks, inp)
    if valid:
        return True
    return False


try:
    obj = {}
    size = 0

    for idx, line in enumerate(stdin, start=1):
        line = line.strip()

        if not helper(line):
            continue

        slices = line.split(" ")
        size += int(slices[-1])

        if slices[-2] not in obj:
            obj[slices[-2]] = 1
        else:
            obj[slices[-2]] += 1

        obj = dict(sorted(obj.items()))

        if idx % 10 == 0:
            print(f"File size: {size}")
            for key, value in obj.items():
                print(f"{key}: {value}")
except Exception as err:
    pass
finally:
    print("File size: {}".format(size))
    for key, value in obj.items():
        print("{}: {}".format(key, value))
