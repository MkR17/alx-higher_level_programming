#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """This Function returns True or False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        if obj is an instance of a_class, True
        otherwise, False
    """
    return isinstance(obj, a_class)
