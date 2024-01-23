#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    Class that defines properties of a square.

    Attributes:
        size: size of a square(1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            size (int): size of the square (1 side).
            position (tuple): position of the square.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of square.

        Returns:
            the current square area.
        """
        return self.size ** 2

    @property
    def size(self):
        """Returns the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0..
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter fr position.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tupleof 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__osition = value
   
    def my_print(self):
       """prints the square with the character '#'."""
       if self.__size == 0:
           print()
       else:
           for _ in range(self.__position[1]):
               print()
           for _ in range(self.__size):
               for _ in range(self.__position[0]):
                   print(" ", end="")
               print("#" * self.__size)

