#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve 'n' 'H' characters.

    :param n: The target number of 'H' characters.
    :type n: int
    :return: The fewest number of operations required to achieve 'n' 'H' characters.
             If 'n' is impossible to achieve, it returns 0.
    :rtype: int
    """
    if n <= 1:
        # If 'n' is less than or equal to 1, it's impossible to achieve,
        # so return 0 (no operations required).
        return n

    factors = []
    d = 2

    while d <= n:
        if n % d == 0:
            # If 'd' is a factor of 'n', append it to the 'factors' list.
            factors.append(d)
            n //= d
        else:
            d += 1

    # Return the sum of the factors in the 'factors' list,
    # representing the fewest number of operations required to achieve 'n' 'H' characters.
    return sum(factors)

