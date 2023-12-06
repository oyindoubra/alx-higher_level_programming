#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        raise Exception
    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Raises:
            TypeError: If value is not an integer
            ValueError: parameter
        """
        if type(value) != int:
            raise TypeError("{} integer".format(name))
        if value <= 0:
            raise ValueError("{} greater than 0".format(name))
