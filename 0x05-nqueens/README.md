# 0x05-nqueens Project

+ [x] The N queens puzzle
+ This is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
+ Script [0-nqueens.py](0-nqueens.py) has codes that meets the following Instructions.

    + Usage: `nqueens N`
      + If the user called the program with the wrong number of arguments, print  `Usage: nqueens N`, followed by a new line, and exit with the status `1`
    + where N must be an integer greater or equal to `4`
        + If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
        + If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
    + The program should print every possible solution to the problem
        + One solution per line
        + Format: see example
        + You don’t have to print the solutions in a specific order
    + You are only allowed to import the `sys` module
    + Sample compilation of [0-nqueens.py](0-nqueens.py)
      
    ```
        root@ba65c46144e7:/alx-interview/0x05-nqueens# ./0-nqueens.py 4
        [[0, 1], [1, 3], [2, 0], [3, 2]]
        [[0, 2], [1, 0], [2, 3], [3, 1]]
        root@ba65c46144e7:/alx-interview/0x05-nqueens# ./0-nqueens.py 7
        [[0, 0], [1, 2], [2, 4], [3, 6], [4, 1], [5, 3], [6, 5]]
        [[0, 0], [1, 3], [2, 6], [3, 2], [4, 5], [5, 1], [6, 4]]
        [[0, 0], [1, 4], [2, 1], [3, 5], [4, 2], [5, 6], [6, 3]]
        [[0, 0], [1, 5], [2, 3], [3, 1], [4, 6], [5, 4], [6, 2]]
        [[0, 1], [1, 3], [2, 0], [3, 6], [4, 4], [5, 2], [6, 5]]
        [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4], [6, 6]]
        [[0, 1], [1, 4], [2, 0], [3, 3], [4, 6], [5, 2], [6, 5]]
        [[0, 1], [1, 4], [2, 2], [3, 0], [4, 6], [5, 3], [6, 5]]
        [[0, 1], [1, 4], [2, 6], [3, 3], [4, 0], [5, 2], [6, 5]]
        [[0, 1], [1, 5], [2, 2], [3, 6], [4, 3], [5, 0], [6, 4]]
        [[0, 1], [1, 6], [2, 4], [3, 2], [4, 0], [5, 5], [6, 3]]
        [[0, 2], [1, 0], [2, 5], [3, 1], [4, 4], [5, 6], [6, 3]]
        [[0, 2], [1, 0], [2, 5], [3, 3], [4, 1], [5, 6], [6, 4]]
        [[0, 2], [1, 4], [2, 6], [3, 1], [4, 3], [5, 5], [6, 0]]
        [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3], [6, 6]]
        [[0, 2], [1, 6], [2, 1], [3, 3], [4, 5], [5, 0], [6, 4]]
        [[0, 2], [1, 6], [2, 3], [3, 0], [4, 4], [5, 1], [6, 5]]
        [[0, 3], [1, 0], [2, 2], [3, 5], [4, 1], [5, 6], [6, 4]]
        [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2], [6, 6]]
        [[0, 3], [1, 1], [2, 6], [3, 4], [4, 2], [5, 0], [6, 5]]
        [[0, 3], [1, 5], [2, 0], [3, 2], [4, 4], [5, 6], [6, 1]]
        [[0, 3], [1, 6], [2, 2], [3, 5], [4, 1], [5, 4], [6, 0]]
        [[0, 3], [1, 6], [2, 4], [3, 1], [4, 5], [5, 0], [6, 2]]
        [[0, 4], [1, 0], [2, 3], [3, 6], [4, 2], [5, 5], [6, 1]]
        [[0, 4], [1, 0], [2, 5], [3, 3], [4, 1], [5, 6], [6, 2]]
        [[0, 4], [1, 1], [2, 5], [3, 2], [4, 6], [5, 3], [6, 0]]
        [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1], [6, 6]]
        [[0, 4], [1, 6], [2, 1], [3, 3], [4, 5], [5, 0], [6, 2]]
        [[0, 4], [1, 6], [2, 1], [3, 5], [4, 2], [5, 0], [6, 3]]
        [[0, 5], [1, 0], [2, 2], [3, 4], [4, 6], [5, 1], [6, 3]]
        [[0, 5], [1, 1], [2, 4], [3, 0], [4, 3], [5, 6], [6, 2]]
        [[0, 5], [1, 2], [2, 0], [3, 3], [4, 6], [5, 4], [6, 1]]
        [[0, 5], [1, 2], [2, 4], [3, 6], [4, 0], [5, 3], [6, 1]]
        [[0, 5], [1, 2], [2, 6], [3, 3], [4, 0], [5, 4], [6, 1]]
        [[0, 5], [1, 3], [2, 1], [3, 6], [4, 4], [5, 2], [6, 0]]
        [[0, 5], [1, 3], [2, 6], [3, 0], [4, 2], [5, 4], [6, 1]]
        [[0, 6], [1, 1], [2, 3], [3, 5], [4, 0], [5, 2], [6, 4]]
        [[0, 6], [1, 2], [2, 5], [3, 1], [4, 4], [5, 0], [6, 3]]
        [[0, 6], [1, 3], [2, 0], [3, 4], [4, 1], [5, 5], [6, 2]]
        [[0, 6], [1, 4], [2, 2], [3, 0], [4, 5], [5, 3], [6, 1]]
        root@ba65c46144e7:/alx-interview/0x05-nqueens# ./0-nqueens.py 6
        [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
        [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
        [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
        [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
        root@ba65c46144e7:/alx-interview/0x05-nqueens#
    ```
+ [x] Read:
    + [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29)
    
    + [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
