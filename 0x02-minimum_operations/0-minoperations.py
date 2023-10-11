#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve 'n' 'H' characters.
    """
    if n <= 1:
        return n

    factors = []
    d = 2

    while d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1

    return sum(factors)

