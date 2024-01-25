#!/usr/bin/python3
''' 0. Log parsing: solution '''

import sys


def helper(codes, size):
    '''helper function'''
    print("File size: {}".format(size))
    for key, value in sorted(codes.items()):
        if value != 0:
            print(f"{key}: {value}")


if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    counts = 0
    try:
        for line in sys.stdin:
            counts += 1
            data = line.split()
            try:
                file_size += int(data[-1])
            except:
                pass
            try:
                status_codes[data[-2]] += 1
            except:
                pass
            if counts % 10 == 0:
                print_stats(status_codes, file_size)
        print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
