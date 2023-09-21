# for i in range(100):
#     print('Я буду инжинером програмистом')


# import math
#
# l = 4
# w = 10
# d = math.sqrt(l**2 + w**2)
# print(d)


# print((2 * 3) - (2**2))

# home = "Russia"
# if home == "Russia":
#     print(f"Привет {home}")
# else:
#     print("Привет бомж")


# print(10 % 2)
# print(10 / 2)
# print(10 // 2)

# x = 2
# if x == 2:
#     print(f"Число: {x}")
# if x % 2 == 0:
#     print("Число четное")
# if x % 2 != 0:
#     print("Число нечетное")

# x = 10
# y = 11
# if x == 10:
#     if y == 12:
#         print(x + y)
#     else:
#         print('ничего не вышло')

# home = 'Тайланд'
# if home == 'Япония':
#     print('привет Япония')
# elif home == 'Тайланд':
#     print('привет Тайланд')
# elif home == 'Индия':
#     print('привет Индия')
# elif home == 'Китай':
#     print('Китай')
# else:
#     print('Привет мир')


# home = 'Марс'
# if home == 'россия':
#     print('Привет россия')
# elif home == 'Казахстан':
#     print('привет казахстан')
# elif home == 'Тайнланд':
#     print('Привет Тайнланд')
# elif home == 'Мексика':
#     print('Привет Мексика')
# else:
#     print('привет мир')


# x = 100
# if x == 10:
#     print('10')
# elif x == 20:
#     print('20')
# else:
#     print('не знаю')
# if x == 100:
#     print('x == 100')
# if x % 2 == 0:
#     print('x четное')
# else:
#     print('x нечетное')

# практикум

# print('выше')
# print('и')
# print('ниже')

# a = 40
# if a < 10:
#     print(f'{a} меньше 10')
# else:
#     print(f'{a} больше или равно 10')

# any_random = 40
# if any_random <= 10:
#     print(f'{any_random} меньше или равно 10')
# elif any_random <= 25:
#     print(f'{any_random} больше 10, но меньше или равно 25')
# else:
#     print(f'{any_random} больше 25')

# a = 23
# b = 4
# print(a % b)

# a = 19
# b = 10
# print(a / b)

# age = 30
# if age == 30:
#     print(f'вам {age}')
# if age % 2 == 0:
#     print('Число четное')
# else:
#     print(f"Вам {age},а это больше 30")


# Функции


# def calculation(x, y):
#     z = x + y
#     return z
#
#
# a = calculation(10, 20)
# b = calculation(13, 40)
# c = calculation(5, 5)
# d = a + b + c
# print(d)


# def even(x):
#     return x % 2 == 0
#
#
# for i in range(1, 100):
#     print(i, even(i))

# def f(x):
#     return x + 1
#
#
# z = f(5)
# if z == 5:
#     print('z равно 5')
# else:
#     print('z не равно 5')

# def f(x, y, z):
#     return x + y + z
#
#
# result = f(1, 2, 3)
# print(result)

# def f():
#     z = 1 + 1
#
#
# result = f()
# print(result)


# age = input('укажите возраст: ')
# int_age = int(age)
# if int_age < 21:
#     print('вы молоды')
# else:
#     print('ну вы и старик')


# def even_dd(x):
#     if x % 2 == 0:
#         print('четное')
#     else:
#         print('нечетное')
#
#
# even_dd(2)
# even_dd(3)
# even_dd(5)
#
#
# temperature = int(input('сколько гразудусов на улице: '))
# run = 0
# while temperature >= 15:
#     run += 20
#     temperature -= 2
#     if temperature <= 15:
#         break
#     run += 10
#
# print(temperature)
# print(run)

# Обработка исключений
# try:
#     a = input('ввод: ')
#     b = input('ввод: ')
#     a = int(a)
#     b = int(b)
#
#     print(a / b)
# except (ZeroDivisionError, ValueError):
#     print('делить на 0 нельзя')

# Практикум
# 1. Напишите функцию, которая принимает число в качестве ввода, возводит
# его в квадрат и возвращает.
# 2. Создайте функцию, которая принимает строку в качестве параметра и воз-
# вращает ее.
# 3. Напишите функцию, которая принимает три обязательных и два необяза-
# тельных параметра.
# 4. Напишите программу с двумя функциями. Первая функция должна при-
# нимать в качестве параметра целое число и возвращать результат деления
# этого числа на 2. Вторая функция должна принимать в качестве параметра
# целое число и возвращать результат умножения этого числа на 4. Вызовите
# первую функцию, сохраните результат в переменной и передайте ее в каче-
# стве параметра во вторую функцию.
# 5. Напишите функцию, которая преобразовывает строку в тип данных  oat и
# возвращает результат. Используйте обработку исключений, чтобы перехва-
# тить возможные исключения.
# 6. Добавьте строку документации ко всем функциям, которые вы написали в за-
# даниях 1–5.
# ----
# def f(x):
#     return x ** 2
#
#
# print(f(2))
# ----
# def return_string(string):
#     print(string)
#
# return_string('Это текст')
# ----
# def test(a):
#     return a + 5
#
# result = test(5)
#
# if result == 10:
#     print('тест == 10')
# else:
#     print('тест != 5')
# ----

# def add_mult(a, b, c, d=100, f=1000):
#     return a + b + c * d * f
#
#
# result = add_mult(10, 15, 25)
# print(result)
# ----
# def greet(name, age, city, gender=None, occupatiom=None):
#     print(f'Привет {name}, тебе {age} лет и ты живешь в {city}')
#     if gender:
#         print(f'Твой пол {gender}')
#     if occupatiom:
#         print(f'Ты работаешь {occupatiom}')
# #
#
# greet('Алекс', 25, 'Турция', 'Петушок', 'QA')

# def one(a):
#     return a / 2
#
#
# def two(a):
#     return a * 4
#
#
# result = one(10)
# print(result)
#
# results = two(result)
# print(results)

def convert(string):
    try:
        return float(string)
    except ValueError:
        print('Не удалось преобразовать строку в число с плавающей точкой')


c = convert('d')
print(c)
