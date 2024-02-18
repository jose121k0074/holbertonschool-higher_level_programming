#!/usr/bin/python3
"""
A model that contains a Rectagle class
"""

from models.base import Base


class Rectangle(Base):
    """
    Init class rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The __init__ method initializes the size value
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        ...
        """
        return self.__width

    @width.setter
    def width(self, param):
        """
        ...
        """

        self.__width = param

    @property
    def height(self):
        """
        ...
        """
        return self.__height

    @height.setter
    def height(self, param):
        """
        ...
        """

        self.__height = param

    @property
    def x(self):
        """
        ...
        """
        return self.__x

    @x.setter
    def x(self, param):
        """
        ...
        """

        self.__x = param

    @property
    def y(self):
        """
        ...
        """
        return self.__y

    @y.setter
    def y(self, param):
        """
        ...
        """

        self.__y = param
