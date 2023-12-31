#!/usr/bin/python3
class Square:
    """ The class that defines a square by its size
    """
    def __init__(self, size=0):
        """ Method initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method returns the square are of the object
        """
        return (self.__size ** 2)
