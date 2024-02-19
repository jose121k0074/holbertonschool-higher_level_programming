#!/usr/bin/python3
"""
A Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Init class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        The __init__ method initializes the size value
        """
        
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        ...
        """

        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        ...
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        ...
        """

        self.width = value
        self.height = value
