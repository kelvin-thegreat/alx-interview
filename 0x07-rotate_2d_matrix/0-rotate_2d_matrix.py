#!/usr/bin/python3
"""2D matrix rotation module.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates an m by n 2D matrix in place.
    :param matrix: The 2D matrix to be rotated
    :type matrix: list of lists
    """
    # Check if the input is a valid matrix
    if not isinstance(matrix, list) or len(matrix) <= 0 or not all(isinstance(row, list) for row in matrix):
        return

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Check if all rows have the same number of columns
    if not all(len(row) == num_cols for row in matrix):
        return

    # Initialize variables for traversal
    current_col, current_row = 0, num_rows - 1

    # Create a new matrix to store the rotated elements
    rotated_matrix = []

    # Traverse the original matrix and copy elements to the new matrix in the desired order
    for i in range(num_cols * num_rows):
        # If a new row needs to be started in the new matrix
        if i % num_rows == 0:
            rotated_matrix.append([])

        # Copy the element to the new matrix
        rotated_matrix[-1].append(matrix[current_row][current_col])

        # Move to the next element in the original matrix
        current_row -= 1

        # If we reach the end of a column, move to the next column
        if current_row == -1:
            current_row = num_rows - 1
            current_col += 1

    # Update the original matrix with the rotated elements
    matrix[:] = rotated_matrix
