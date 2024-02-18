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

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

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
        self.check_integer_parameter(param, 'width')

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
        self.check_integer_parameter(param, 'height')

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
        self.check_integer_parameter(param, 'x')

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
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """
        ...
        """
        return self.__width * self.__height

    def display(self):
        """
        ...
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)
