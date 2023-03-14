#!/usr/bin/python3
"""Module 12-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.

    Args:
        n: size of the triangle (rows)

    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    result = [[1]]
    while len(result) is not n:
        tmp = [1]
        for i in range(len(result[-1]) - 1):
            tmp.append(result[-1][i] + result[-1][i + 1])
        tmp.append(1)
        result.append(tmp)
    return result
