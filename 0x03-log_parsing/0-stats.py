#!/usr/bin/python3
''' 0. Log parsing: solution '''
import sys


def print_stats(status_codes, file_size):
    '''Prints the stats function'''
    print(f"File size: {file_size}")
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


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
