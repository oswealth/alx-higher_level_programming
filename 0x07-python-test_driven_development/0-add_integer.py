#!/usr/bin/python3
"""

This module is comprises a function that adds two numbers

"""

def add_integer(a, b=98):

    """Add two integers and return the result.
    Parameters:
    a (int or float): The first addend.
    b (int or float): The second addend. Defaults to 98.

    Returns:
    int: The sum of a and b as an integer.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
