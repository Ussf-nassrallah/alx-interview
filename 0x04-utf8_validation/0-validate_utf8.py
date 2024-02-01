#!/usr/bin/python3
"""
0. UTF-8 Validation: task solution
"""


def validUTF8(data):
    ''' validUTF8(data) '''

    num_bytes = 0

    lead_bite = 1 << 7
    trai_bite = 1 << 6

    for byte in data:
        current_bite = 1 << 7

        if num_bytes == 0:
            while current_bite & byte:
                num_bytes += 1
                current_bite = current_bite >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & lead_bite and not (byte & trai_bite)):
                return False

        num_bytes -= 1

    return num_bytes == 0
