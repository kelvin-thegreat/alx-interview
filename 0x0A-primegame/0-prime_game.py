#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds in the game.
        nums (List[int]): An array of integers representing the range for each round.

    Returns:
        str or None: The name of the player that won the most rounds (either 'Maria' or 'Ben').
                     If the winner cannot be determined, returns None.

    Note:
        The function assumes that Maria always goes first and both players play optimally.
        It also ensures that the provided inputs adhere to the specified constraints.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'

