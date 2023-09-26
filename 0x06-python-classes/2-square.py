#!/usr/bin/python3

"""a class Square that defines a square by: q1"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize  new Square.

        Args:
        size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
