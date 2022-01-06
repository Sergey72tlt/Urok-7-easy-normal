#Митягин Сергей сложность Easy

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle(object):

    def __init__(self, a, b, c):
        self.side_A = a
        self.side_B = b
        self.side_C = c

    def calc_perimeter(self):
        p = self.side_A + self.side_B + self.side_C
        return p

    def calc_height(self):
        h = 2 * self.calc_square() / self.side_A
        return h

    def calc_square(self):
        p = (self.side_A + self.side_B + self.side_C) / 2
        s = math.sqrt(p * (p - self.side_A) * (p - self.side_B) * (p - self.side_C))
        return s


triangle_obj = Triangle(10, 14, 9)
print('p = ', triangle_obj.calc_perimeter())
print('s = ', triangle_obj.calc_square())
print('h = ', triangle_obj.calc_height())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid(object):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.ab = self.calculate_side(a, b)
        self.bc = self.calculate_side(b, c)
        self.cd = self.calculate_side(c, d)
        self.da = self.calculate_side(d, a)

    def calculate_side(self, tochka1, tochka2):
        x1 = tochka1[0]
        y1 = tochka1[1]
        x2 = tochka2[0]
        y2 = tochka2[1]

        side = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return side

    def is_ravnobochnaya(self):
        if self.ab == self.cd:
            return True
        else:
            return False

    def calculate_perimetr(self):
        return self.ab + self.bc + self.cd + self.da

    def calculate_hight(self):
        return 0.5 * math.sqrt(4 * self.ab ** 2 - (self.bc - self.da) ** 2)

    def calculate_square(self):
        s = 0.5 * self.calculate_hight() * (self.bc + self.da)
        return s


trapecia = Trapezoid((1, 1), (2, 5), (4, 5), (5, 1))
print('h = ', trapecia.calculate_hight())
print('p = ', trapecia.calculate_perimetr())
print('s = ', trapecia.calculate_square())
