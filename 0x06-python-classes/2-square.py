#!/usr/bin/python3
"""This module defines a class Square. """


class Square:
    """ a square with a private attribute size."""
	
	def __init__(self, size=0):
		""" initializes a square object with its size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
