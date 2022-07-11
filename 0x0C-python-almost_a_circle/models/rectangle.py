#!/usr/bin/python3
""" Module that contains class Rectangle,
inheritance of class Base
"""
from models.base import Base

class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("width must be int")
        if type(height) != int:
            raise TypeError("width must be int")
        if type(x) != int:
            raise TypeError("width must be int")
        if type(y) != int:
            raise TypeError("width must be int")
        if width <=0:
            raise ValueError("width must be >= 0")
        if width <=0:
            raise ValueError("width must be >= 0")
        if width <=0:
            raise ValueError("width must be >= 0")
        if width <=0:
            raise ValueError("width must be >= 0")
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter """
        return self.__width
    @width.setter
    def width(self, value):
        """width setter"""
         if width <=0:
            raise ValueError("width must be >= 0")
       
        self.__width = value
    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.__height = value
    @property
    def x(self):
        """ x getter """
        return self.__x
    @x.setter
    def x(self, value):
        """ x setter """
        self.__x = value
    @property
    def y(self):
       """ y getter """
       return self.__y
    @y.setter
    def y(self, value):
       """ y setter """
       self.__y = value
       
def area(self):
    return self.width() * self.height()
def display(self):
    for i in range(self.height):
        for j in range(self.width):
            print("#", end ="")
        print("", end="\n")    
