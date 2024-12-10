#!/usr/bin/python3
"""
Module for generating Pascal's Triangle using an alternative method
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows using an alternative method.

    Args:
        n (int): Number of rows to generate

    Returns:
        list of lists: Pascal's Triangle represented as a list of lists of int
    """
    if n <= 0:
        return []

    result = [[1]]
    for _ in range(1, n):
        prev_row = result[-1]
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)
        result.append(new_row)

    return result
