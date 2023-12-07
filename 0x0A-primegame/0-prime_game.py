#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Determines the winner of each round and overall winner."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(limit):
        primes = []
        for i in range(2, limit + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def calculate_winner(round_nums):
        primes = get_primes(max(round_nums))
        round_nums_set = set(round_nums)

        maria_wins = True
        for prime in primes:
            if any(num % prime == 0 for num in round_nums_set):
                maria_wins = not maria_wins

        return "Maria" if maria_wins else "Ben"

    winners = [calculate_winner(list(range(1, num + 1))) for num in nums]

    maria_wins_count = winners.count("Maria")
    ben_wins_count = winners.count("Ben")

    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    # Test the example
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
