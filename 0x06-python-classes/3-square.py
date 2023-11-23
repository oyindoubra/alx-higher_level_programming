#!/usr/bin/python3
"""class Square defining square"""


class Square():
    """square class with the size and proper validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be in integer")
        elif (size < 0):
            raise ValueError("size must be greater than or equal to 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
