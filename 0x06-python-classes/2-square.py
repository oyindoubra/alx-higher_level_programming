#!/usr/bin/python3
"""class square that defining a square"""


class Square():
    """square class with d size and proper validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be in integer")
        elif (size < 0):
            raise ValueError("size must be greater than or equal to 0")
        self.__size = size
