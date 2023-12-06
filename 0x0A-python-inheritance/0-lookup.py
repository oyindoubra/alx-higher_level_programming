#!/usr/bin/python3
"""Defines an object attribute lookup function"""



def lookup(obj):
    """Return list of an objects available attributes"""
    return (dir(obj))
