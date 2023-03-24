#!/usr/bin/python3
"""
0-pascal_triangle.py: pascal_triangle()
"""


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal’s triangle of n
    """
    pt_list = []
    if (n <= 0):
        return new_list
    pt_list.append([1])
    for i in range(n - 1):
        pt_list.append([1] + [pt_list[i][a] + pt_list[i][a + 1]
                              for a in range(len(pt_list[i]) - 1)] + [1])
    return pt_list
