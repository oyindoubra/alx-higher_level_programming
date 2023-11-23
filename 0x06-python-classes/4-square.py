#!/usr/bin/python3
"""class Square defining a square"""


class Square():
    """square class with the size and proper validation"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be in integer")
        elif (value < 0):
            raise ValueError("size must be greater than or equal to 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
