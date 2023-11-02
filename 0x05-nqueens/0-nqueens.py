#!/usr/bin/python3
"""N queens solution finder module."""

import sys

queen_solutions = []
"""List to store possible solutions to the N queens problem."""

board_size = 0
"""The size of the chessboard."""

queen_positions = None
"""List to store possible positions on the chessboard."""

def get_board_size():
    """Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global board_size
    board_size = 0

    # Check if the correct number of arguments is provided.
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Attempt to convert the argument to an integer.
    try:
        board_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    # Ensure that the chessboard size is at least 4.
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    return board_size

def is_attacking(position1, position2):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        position1 (list or tuple): The first queen's position.
        position2 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    return (position1[0] == position2[0]) or (position1[1] == position2[1]) or (abs(position1[0] - position2[0]) == abs(position1[1] - position2[1))

def group_exists(existing_group):
    """Checks if a group exists in the solutions.

    Args:
        existing_group (list of integers): Possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global queen_solutions

    # Check if the given group of positions exists in the solutions.
    return any(all(solution_pos[0] == group_pos[0] and solution_pos[1] == group_pos[1] for group_pos in existing_group) for solution in queen_solutions)

def build_solution(row, group):
    """Builds a solution.

    Args:
        row (int): The current row.
        group (list of lists of integers): Valid positions.
    """
    global queen_solutions
    global board_size

    if row == board_size:
        temporary_group = group.copy()

        # Add the solution to the list if it does not already exist.
        if not group_exists(temporary_group):
            queen_solutions.append(temporary_group)
    else:
        for col in range(board_size):
            a = (row * board_size) + col
            matches = list(zip([queen_positions[a]] * len(group), group))
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(queen_positions[a].copy())

            # Recursively build the solution if no attacking positions are found.
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop()

def find_solutions():
    """Solves the N-queens problem for the given chessboard size.
    """
    global queen_positions, board_size
    queen_positions = list(map(lambda x: [x // board_size, x % board_size], range(board_size ** 2)))
    row = 0
    solution_group = []
    build_solution(row, solution_group)

board_size = get_board_size()
find_solutions()

# Print the solutions.
for solution in queen_solutions:
    print(solution)
