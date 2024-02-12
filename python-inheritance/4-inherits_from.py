#!/usr/bin/python3
"""define function"""


def inherits_from(obj, a_class):
	"""
    initializes some values

    """

    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
