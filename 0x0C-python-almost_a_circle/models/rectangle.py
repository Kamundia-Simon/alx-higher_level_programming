#!/usr/bin/python3

"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new rectangle

        Args:
            width: width of the new rectangle
            height: height of the new rectangle
            x: x coordinate of the new rectangle
            y: y coordinate of the new rectangle
            id: identity of the new rectangle
        Raises:
            TypeError: if either of width/height is not an integer
            ValueError: if either of width/height less than or equal 0
            TypeError: if either of x/y is not an integer
            ValueError: if either of x/y less than 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.width * self.height
