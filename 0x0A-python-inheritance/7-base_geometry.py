#!/usr/bin/python3
class BaseGeometry:
    """This Class  defines the attributes of Geometric Shapes """

    def area(self):
        """This Method defines the area of a geomtric shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This Method recieves the value property

        Árgs:
            name:The name of the object
            value:The value of the property

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
