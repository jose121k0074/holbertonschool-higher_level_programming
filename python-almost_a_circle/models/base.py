#!/usr/bin/python3
"""

A model that contains a Base class

"""


from os import path
import json


class Base:
    """
    Init Base Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        The __init__ method initializes the size value
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
