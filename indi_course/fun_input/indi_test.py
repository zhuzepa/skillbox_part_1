"""
Напишите программу, которая принимает на вход возраст человека (количество полных лет) и выводит сколько лет
ему исполнится в следующем году
"""
# version 1
# year_people = int(input())
# year_people += 1
# print(year_people)
#
# # version 2
# print(int(input()) + 1)

"""
Вашей программе поступает на вход натуральное число. Ваша задача вывести в отдельных строках:
число, увеличенное в 2 раза;
число, уменьшенное в 2 раза
"""

# a = int(input())
# print(a * 2, a / 2, sep='\n')

"""
Я думаю каждый знаком с квадратом - идеально симметричная и ровная фигура. Давайте напишем программу,
 которая вычисляет площадь квадрата по введенной длине.
"""
# a = float(input())
# print(a ** 2)

"""
Напишите программу, которая принимает на вход два целых числа в отдельных строках и выводит на экран их сумму.
"""
# a = int(input())
# b = int(input())
# print(a + b)

# print(int(input()) + int(input()))

"""
В этом задании необходимо написать программу, которая вычисляет площадь и периметр прямоугольника по введенной длине и ширине.
"""

# a, b = float(input()), float(input())
# print(a * b, 2 * (a + b))


"""
Из Фаренгейтов в градусы Цельсия
"""
# temperature_fahrenheit = float(input('Введите темпиратуру: '))
# print((temperature_fahrenheit - 32) * 5 / 9)


"""
Найдите результат выражения ∣a∣+∣b∣
Значения переменных а и b поступают на вход в отдельных строках и могут быть только целого типа
"""
# a, b = int(input()), int(input())
# print(abs(a) + abs(b))

"""
Напишите программу, которая вычисляет длину отрезка (т.е. расстояние между двумя точками), заданного двумя значениями x1 и x2 (вещественные числа).
"""
# a, b = float(input()), float(input())
# print(abs(a - b))

"""
Вводится вещественное число и нам нужно его округлить до 2 и 3 разряда после запятой и вывести полученный результат через пробел в одной строчке
"""
# a = float(input())
# print(round(a, 2), round(a, 3))

"""
Разность времен
"""
# a1, b1, c1, d1, e1, f1 = map(float, input().split())
# print(abs(a1 + b1 + c1) - (d1 + e1 + f1))

# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# d1 = int(input())
# e1 = int(input())
# f1 = int(input())
#
# t1 = a1 * 3600 + b1 * 60 + c1
# t2 = d1 * 3600 + e1 * 60 + f1
# print(t2 - t1)
#
# version
# time1 = int(input()) * 3600 + int(input()) * 60 + int(input())
# time2 = int(input()) * 3600 + int(input()) * 60 + int(input())
# print(time2 - time1)


# a = int(input())
# b = int(input())
# a, b, c = map(int, input().split())
# print(a, b, c)
# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a + b + c, a * b * c, a + b * c, a * b + c, (a + b) * c, a * (b + c)))

# a, b, c, d = map(int, input().split())  # считываем 3 целых числа через пробел
# print((a + b + c + d) / 4)

#Найти лучшую оценку
# a, b, c, d, e = map(int, input().split())
# print(max(a, b,  c, d, e))

# n, a, b = map(int, input().split())
# print(n * a * b * 2)

#Журавлики

# s = int(input())
# x = s // 6
# print(x, x*4, x)


# import math
# print(4306634.4 / 1000)
# print(4306634.4 / 1000)
# print(round(4306.5))
# print(round(4.47))
# m = math.ceil(4.47)
# print(m)

# Магазин канцелярских товаров
# x, y, z = map(int, input().split())
# print(x * 3 + y * 5 + z * 12)

# Два бандита
a, b = map(int, input().split())
c = a + b - 1
print(c-a, c-b)