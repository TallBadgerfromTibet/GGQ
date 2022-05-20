# 1. Создать класс Figure (фигура) с атрибутом уровня класса unit (единица измерения величин) и присвоить ему значение cm (сантиметры) или mm (миллиметры)
class Figure:
    unit = 'cm'

    def __init__(self, ploshad=0, perimeter=0):
        self.__ploshad = ploshad
        self.__perimeter = perimeter

    # 2. Создать приватный атрибут perimeter в классе Figure, который бы по умолчанию в конструкторе присваивался к нулю.
    # 3. Создать в классе Figure геттер и сеттер для атрибута perimeter.
    # 4. В конструкторе класса Figure должен быть только 1 входящий параметр self.
    # 5. Добавить в класс Figure нереализованный публичный метод calculate_area (подсчет площади фигуры)
    # 6. Добавить в класс Figure нереализованный приватный метод calculate_perimeter (подсчет периметра фигуры)
    # 7. Добавить в класс Figure нереализованный публичный метод info (вывод полной информации о фигуре)
    # 8. Создать класс Square (квадрат), наследовать его от класса Figure.
    # 9. Добавить в класс Square атрибут side_length (длина одной стороны квадрата), атрибут должен быть приватным.
    @property
    def perimeter(self, value):
        self.__perimeter = value

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):

    def __init__(self, side_length):
        self.__side_length = side_length

    def __calculate_area(self):
        return f'square: {self.__side_length * 2}'

    def __calculate_perimeter(self):
        return f'perimeter: {self.__side_length * 4}'

    def info(self):
        print(f'Square: \n'
              f'Side length: {self.__side_length} \n'
              f'Area: {self.calculate_area()} \n'
              f'Perimeter: {self.calculate_perimeter()} \n')


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__side_length = None
        self.__length = length
        self.__width = width
        self.perimeter = self.calculate_perimeter()

    def __calculate_area(self):
        return f'square: {self.__side_length * 2}'

    def __calculate_perimeter(self):
        return f'perimeter: {self.__side_length * 4}'
        
    def info(self):
        print(f'Square: \n'
              f'Side length: {self.__side_length} \n'
              f'width: {self.__side_width}'
              f'Area: {self.calculate_area()} \n'
              f'Perimeter: {self.calculate_perimeter()} \n')



# 10. В конструкторе класса Square должен высчитываться периметр квадрата, посредством вызова метода calculate_perimeter и возвращаемый результат метода задавался бы атрибуту perimeter.
# 11. В классе Square переопределить метод calculate_area, который бы считал и возвращал площадь квадрата.
# 12. В классе Square переопределить метод calculate_perimeter, который бы считал и возвращал периметр квадрата.
# 13. В классе Square переопределить метод info, который бы распечатывал всю информацию о квадрате следующим образом: Например - Square side length: 5cm, perimeter: 20cm, area: 25cm.
# 14. Создать класс Rectangle (прямоугольник), наследовать его от класса Figure.
# 15. Добавить в класс Rectangle атрибут length (длина) и width (ширина), атрибуты должны быть приватными.
# 16. В конструкторе класса Rectangle должен высчитываться периметр прямоугольника, посредством вызова метода calculate_perimeter и возвращаемый результат метода задавался бы атрибуту perimeter.
# 17. В классе Rectangle переопределить метод calculate_area, который бы считал и возвращал площадь прямоугольника.
# 18. В классе Rectangle переопределить метод calculate_perimeter, который бы считал и возвращал периметр прямоугольника.
# 19. В классе Rectangle переопределить метод info, который бы распечатывал всю информацию о прямоугольнике следующим образом: Например - Rectangle length: 5cm, width: 8cm, perimeter: 26cm, area: 40cm.
# 20. В исполняемом файле создать список из 2-х разных квадратов и 3-х разных прямоугольников 21. Затем через цикл вызвать у всех объектов списка метод info
