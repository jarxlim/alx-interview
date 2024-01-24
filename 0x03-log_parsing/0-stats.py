#!/usr/bin/python3

import sys


def prints_info(_dict, size):
    """ prints information """
    print("File size: {:d}".format(size))
    for i in sorted(_dict.keys()):
        if _dict[i] != 0:
            print("{}: {:d}".format(i, _dict[i]))


sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            prints_info(sts, size)

        s_list = line.split()
        count += 1

        try:
            size += int(s_list[-1])
        except:
            pass

        try:
            if s_list[-2] in sts:
                sts[s_list[-2]] += 1
        except:
            pass
    prints_info(sts, size)


except KeyboardInterrupt:
    prints_info(sts, size)
    raise
