#!/usr/bin/python3
def lookup(obj):
    """This Function returns the list of available attributes
        and methods of an object

    Args:
        obj:is instance of the class

    Returns:
       A List of attributes
    """

    return dir(obj)
