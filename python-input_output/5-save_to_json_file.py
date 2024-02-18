#!/usr/bin/python3
"""save to json a file"""


from json import dumps


def save_to_json_file(my_obj, filename):
    """
    init function
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
