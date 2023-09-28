#!/usr/bin/python3
'''A module for working with Pascal's triangle.'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing'''
    tri = []
    if type(n) is not int or n <= 0:
        return tri
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(tri[i - 1][j - 1] + tri[i - 1][j])
        tri.append(line)
    return tri
