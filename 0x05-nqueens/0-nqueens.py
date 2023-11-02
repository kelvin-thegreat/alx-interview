#!/usr/bin/python3
""" Module to solve N queens problem.
"""
import sys

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at a given position."""
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(n):
    """Solve the N-Queens puzzle using backtracking."""
    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0)
    return solutions

def print_solutions(solutions):
    """Print the N-Queens puzzle solutions."""
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)

