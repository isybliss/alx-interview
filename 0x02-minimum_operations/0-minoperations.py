#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
to result in exactly n number of characters in the file.
"""


def minOperations(n):
    """
    calaculate minimum number of operations to return n number of characters
    n: number of characters to be returned
    Return: number of operations
    """
    if n <= 1:
        return 0

    no_of_operation = 0
    operators = 2

    while n > 1:
        if n % operators == 0:
            n //= operators
            no_of_operation += operators
        else:
            operators += 1
    return no_of_operation
