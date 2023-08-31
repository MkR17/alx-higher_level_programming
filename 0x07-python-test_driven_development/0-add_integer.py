#!/usr/bin/python3
"""

This module contains a function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function adds two integer and/or float numbers

    Args:
        a: the first number
        b: the second number

    Returns:
        The sum of the two given numbers

    Raises:
        TypeError: If a or b are not integers and/or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must always be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must always  be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
