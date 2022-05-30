class Figure:
    unit = 'cm'

    def __init__(self):
        self.__calculate_perimeter()
        self.calculate_area()

    def get_perimeter(self):
        return self.__perimeter

    def set_perimeter(self, perimeter):
        self.__perimeter = perimeter

    def calculate_area(self):
        pass

    def __calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, __side_length):
        self.__side_length = __side_length
        self.calculate_area()
        self.perimeter = self.__calculate_perimeter()

    def calculate_area(self):
        return self.__side_length * 2

    def __calculate_perimeter(self):
        return self.__side_length * 4

    def info(self):
        print(
            f"Square:   Side length:{self.__side_length}{self.unit}   Perimeter:{self.__calculate_perimeter()}{self.unit}   Area:{self.calculate_area()}{self.unit}")


class Rectangle(Figure):

    def __init__(self, __length, __width):
        self.__width = __width
        self.__length = __length

    def calculate_area(self):
        return self.__length * self.__width

    def __calculate_perimeter(self):
        return (self.__length + self.__width) * 2

    def info(self):
        print(
            f"Rectangle: Length:{self.__length}{self.unit}   Width:{self.__width}{self.unit}   Perimeter:{self.__calculate_perimeter()}{self.unit}   Area:{self.calculate_area()}{self.unit}")


sq1 = Square(2)
sq2 = Square(4)

rec1 = Rectangle(5, 8)
rec2 = Rectangle(1, 3)
rec3 = Rectangle(1, 4)

general = [sq1, sq2, rec1, rec2, rec3]
for i in general:
    i.info()
