#!/usr/bin/python3
''' 0. Log parsing: solution '''


from sys import stdin
import re


def valid_format(line):
    """checks if the line have a valid format"""
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    if match:
        return True
    return False


try:
    my_dict = {}
    total_size = 0
    for i, line in enumerate(stdin, start=1):
        line = line.strip()
        if not valid_format(line):
            continue
        parts = line.split(" ")
        total_size += int(parts[-1])
        if parts[-2] not in my_dict:
            my_dict[parts[-2]] = 1
        else:
            my_dict[parts[-2]] += 1
        my_dict = dict(sorted(my_dict.items()))
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in my_dict.items():
                print("{}: {}".format(key, val))
except Exception as err:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, val in my_dict.items():
        print("{}: {}".format(key, val))
