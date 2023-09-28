#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row and return it as a list of lists.
    """
    result = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            coefficient = 1
            for j in range(1, i + 1):
                row.append(coefficient)
                coefficient = coefficient * (i - j) // j
            result.append(row)
    return result
