#!/usr/bin/python3
"""UTF-8 validation module.
"""

def validUTF8(data):
    '''
    Initialize a variable to keep track of the number of bytes left
    for the current character
    '''
    bytes_left = 0

    '''Iterate through each integer in the data list'''
    for num in data:
        ''' Check the two most significant bits of the current byte '''
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
            ''' Check that the current byte is of the form 10xxxxxx'''
            if (num >> 6) != 0b10:
                return False
            bytes_left -= 1
    return bytes_left == 0
