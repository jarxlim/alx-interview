#!/usr/bin/python3

"""
method that calculates the fewest number of operations
"""


def minOperations(n):
    """
    a method that calculates the fewest number of operations needed to result 
    in exactly n H characters in the file.
    """

    run = 1
    start = 0
    count = 0
    while run < n:
        remainder = n - run
        if (remainder % run == 0):
            start = run
            run += start
            count += 2
        else:
            run += start
            count += 1
    return count
