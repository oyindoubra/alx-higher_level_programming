#!/usr/bin/python3
""" an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class

        obj (any): The object to check
        a_class (type): The class to match the type of obj to check
        If obj is an inherited instance of a_class it is True
        Otherwise it is  False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
