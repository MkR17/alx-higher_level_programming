#!/usr/bin/python3
def is_same_class(obj, a_class):
    """This Function returns True or False if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        if type of obj is a_class, True
       otherwise False
    """
    return type(obj) is a_class
