class Shape:
    """
    Базовый класс для всех форм, представляющий объекты с координатами.
    """

    def __init__(self, x=0, y=0):
        """
        Инициализация объекта Shape с координатами (x, y).

        :param x: Координата x.
        :param y: Координата y.
        """
        self.x = x
        self.y = y


class Rectangle(Shape):
    """
    Класс для прямоугольников, являющийся подклассом Shape.
    Содержит ширину и высоту, которые могут быть изменены.
    """

    def __init__(self, width, height, x=0, y=0):
        """
        Инициализация прямоугольника с заданной шириной, высотой и координатами.

        :param width: Ширина прямоугольника.
        :param height: Высота прямоугольника.
        :param x: Координата x.
        :param y: Координата y.
        """
        super().__init__(x, y)
        self._width = width
        self._height = height

    def area(self):
        """
        Получение площади прямоугольника

        :return: площадь
        """
        return self._width * self._height


class Square(Rectangle):
    """
    Класс для квадрата, являющийся подклассом Rectangle.
    Ширина и высота квадрата всегда одинаковы.
    """

    def __init__(self, side, x=0, y=0):
        """
        Инициализация квадрата с заданной стороной и координатами.

        :param side: Длина стороны квадрата.
        :param x: Координата x.
        :param y: Координата y.
        """
        super().__init__(side, side, x, y)

    def area(self):
        """
        Получение площади прямоугольника

        :return: площадь
        """
        return self._width * self._height

    @property
    def width(self):
        """
        Получение ширины квадрата (сторона квадрата).
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Установка ширины квадрата (приводит к изменению и высоты, так как они одинаковы).

        :param value: Новое значение ширины (и высоты).
        """
        self._width = self._height = value

    @property
    def height(self):
        """
        Получение высоты квадрата (сторона квадрата).
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Установка высоты квадрата (приводит к изменению и ширины, так как они одинаковы).

        :param value: Новое значение высоты (и ширины).
        """
        self._height = self._width = value


if __name__ == '__main__':
    a = Square(5)
    print(a.width)
    print(a.height)
    