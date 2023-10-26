#!/usr/bin/python3
"""UTF-8 validation module.
"""

def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    """
    bytes_left = 0

    for num in data:
        if bytes_left == 0:
            if (num >> 5) == 0b110:
                bytes_left = 1
            elif (num >> 4) == 0b1110:
                bytes_left = 2
            elif (num >> 3) == 0b11110:
                bytes_left = 3
            elif (num >> 7) != 0:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            bytes_left -= 1

    return bytes_left == 0
