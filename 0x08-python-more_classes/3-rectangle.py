#!/usr/bin/python3
"""empty rectangle
"""


class Rectangle:
    """empty rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        str = ""
        if self.__width == 0 or self.__height == 0:
            return (str)
        for i in range(self.__height):
            for j in range(self.__width):
                str += "#"
            if i != self.__height - 1:
                str += "\n"
        return (str)

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
