#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve 'n' 'H' characters.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    clipboard = 1
    done = 1

    while done < n:
        if n % done == 0 and done * 2 <= n:
            clipboard = done
            done += clipboard
            operations += 2
        else:
            done += clipboard
            operations += 1

    return operations
