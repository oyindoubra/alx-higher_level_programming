#!/usr/bin/python3
"""Define a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Init a Rectangle

        Args:
            width
            height (int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
