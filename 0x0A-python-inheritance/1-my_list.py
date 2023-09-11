#!/usr/bin/python3
class MyList(list):
    """ This Class inherits the attributes references of class list

    Args:
        list:A class list

    """

    def print_sorted(self):
        """This Method prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
