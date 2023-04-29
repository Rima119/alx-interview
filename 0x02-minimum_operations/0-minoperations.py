#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Returns an integer. If n is impossible to achieve, return 0
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
