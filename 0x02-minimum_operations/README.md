# Minimum Operations Task

This project contains tasks for Minimum Operations Interview Trivia using Python3.

## Tasks
+ [x] 0. **Minimum Operations**<br/>[0-minoperations.py](0-minoperations.py) contains a Python Script that meets the following requirements:
    +  a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy` `All` and `Paste`.Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.
    + Prototype: `def minOperations(n)`
    + Returns an `integer`:
    + If `n` is impossible to achieve, return `0`
    + **Example:**
        + n = `9`
        + H => `Copy All` => `Paste` => HH => `Paste `=>HHH => `Copy All` => `Paste` => HHHHHH => `Paste` => HHHHHHHHH
        + Number of operations: `6`     
    + Use the Script below to testing the code. (save the script to file `0-main.py`)
  ```python3
     	#!/usr/bin/python3
        """
        Main file for testing
        """
        
        minOperations = __import__('0-minoperations').minOperations
        
        n = 4
        print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
        
        n = 12
        print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
  ```     
