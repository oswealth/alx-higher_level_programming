#!/usr/bin/python3
"""checks if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """inherit"""
    if issubclass(type(obj), (a_class)) and type(obj) is not a_class:
        return True
    return False
