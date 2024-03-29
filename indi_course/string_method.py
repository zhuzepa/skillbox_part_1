"""
На вход программе поступает строка, состоящая как из заглавных так из строчных букв латинского алфавита.
Ваша задача преобразовать строку так, чтобы все символы были только заглавными.
"""
# print(input().upper())

"""
На вход программе поступает строка, состоящая как из заглавных так из строчных букв латинского алфавита.
Ваша задача преобразовать строку так, чтобы все символы были только строчными
"""
# print(input().lower())

"""
Программиста Тихона попросили написать программу, которая должна была сравнивать две введенные строки на равенство, при этом не учитывая регистр букв. Если строки вводились одинаковые, программа Тихона должна была печатать True, в противном случае False

Но что-то пошло не так. Тихон написал программу, в которой есть ошибки. Ваша задача исправить имеющуюся программу так, чтобы она прошла все тесты. 
"""
# a, b = input().lower(), input().lower()
# c = a == b
# print(c)
#
# print(input().upper() == input().upper())

"""
На вход подается строка. Ваша задача отформатировать строку так, чтобы первые 3 и последние 3 символа были заглавными, а оставшиеся строчные.

Примечание:
Количество букв может быть различным, но гарантируется что их количество не меньше 6
"""
# s = input()
# b = s[:3].upper()
# c = s[3:-3].lower()
# e = s[-3:].upper()
# print(b+c+e)

"""
На вход программе поступает строка, состоящая как из заглавных так из строчных букв. 
Ваша задача преобразовать строку так, чтобы все строчные символы заменились на заглавные, все заглавные - на строчные.
Символы пунктуации и цифры не нужно преобразовывать.
В качестве ответа нужно вывести полученную строку
"""
# print(input().swapcase())

"""
На вход программе поступает строка, состоящая как из заглавных так из строчных букв. Ваша задача преобразовать строку 
так, чтобы первая буква у каждого слова стала маленькой, а остальные буквы превратились в заглавные. 
Символы пунктуации и цифры не нужно преобразовывать.
В качестве ответа нужно вывести полученную строку
"""
# a = input().swapcase()
# b = a.title()
# c = b.swapcase()
# print(c)

"""
На вход программе поступает строка, ваша задача подсчитать сколько раз в ней встречается латинская буква "e". 
При этом стоит учитывать как маленькие, так и заглавные буквы
"""
# print(input().lower().count('e'))

"""
Какой метод может найти первое слева вхождение символа в строке и вывести индекс этого символа?
"""
# print(input().find('e'))
# print(input().index('e'))

"""
На вход программе поступает строка, ваша задача вывести на экран индекс первой найденной латинской буквы a
Если такого символа в введенной строке нет, выведите -1
"""
# print(input().find('a'))

"""
На вход программе поступает строка, ваша задача вывести на экран индекс последней найденной латинской буквы a
Если такого символа в введенной строке нет, выведите -1
"""
# print(input().rfind('a'))

"""
Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.
Ваша задача заменить все пробелы запятыми и вывести полученную строку.
"""
# print(input().replace(' ', ','))

"""
На вход программе поступает строка, ваша задача удалить из нее все символы w и z.
Учитываем только маленькие буквы
"""
# print(input().replace('w', '').replace('z', ''))

"""
Петя записался в кружок по программированию. На первом занятии Пете задали написать простую программу. 
Программа должна делать следующее: в заданной строке, которая состоит из прописных и строчных латинских букв, она:
удаляет все гласные буквы,
перед каждой согласной буквой ставит символ ".",
все прописные согласные буквы заменяет на строчные.
Гласными буквами считаются буквы A, O, Y, E, U, I, а согласными — все остальные. 
На вход программе подается ровно одна строка, она должна вернуть результат в виде одной строки, получившейся после обработки.
"""
# a = input().lower()
# a = a.replace('a', '').replace('e', '').replace('o', '').replace('y', '').replace('u', '').replace('i', '').replace('o', '')
# a = a.replace('', '.')
# a = a[0:-1]
# print(input().lower().replace('a', '').replace('e', '').replace('o', '').replace('y', '').replace('u', '').replace('i', '').replace('o', '').replace('', '.'))

"""
Программа получает на вход фразу, ваша задача посчитать из скольких слов состоит данная фраза. 
Для удобства будем считать словом любую последовательность символов.
"""
# print(len(input().split()))

"""
Ниже перед вами представлен список list_strings, состоящий из строк. При помощи метода .join и соединителя - получите строку из этих элементов и выведите ее на экран
"""
# list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home']
# print('-'.join(list_strings))

"""
Напишите программу, которая проверяет начинается ли введенная фраза строкой mam вне зависимости от регистра букв
В качестве ответа необходимо вывести True, если введенная строка начинается с mam, во всех остальных случаях нужно вывести False
"""

# print(input().lower().startswith('mam'))

"""
Программа получает на вход две строки, назовем их s и postfix. 
Напишите программу, которая проверяет заканчивается ли введенная фраза s строкой postfix 
"""
# s, suffix = input(), input()
# print(s.end(suffix))

"""
Напишите программу, которая проверяет, чтобы введенная фраза s одновременно начиналась со строки prefix и заканчивалась строкой postfix 
"""
# s, prefix, suffix = input(), input(), input()
# print(s.startswith(prefix) and s.endswith(suffix))

"""
Напишите программу, которая проверяет состоит ли введенная строка целиком из десятичных цифр
В качестве ответа необходимо вывести True, если условие выполняется, во всех остальных случаях нужно вывести False
"""
# print(input().isdigit())

"""
Напишите программу, которая проверяет состоит ли введенная строка целиком из заглавных букв
В качестве ответа необходимо вывести True, если условие выполняется, во всех остальных случаях нужно вывести False
"""
# print(input().isupper())

"""
Напишите программу, которая проверяет состоит ли введенная строка целиком из строчных букв
В качестве ответа необходимо вывести True, если условие выполняется, во всех остальных случаях нужно вывести False
"""
# print(input().islower())

"""
На вход программе поступает строка, состоящая из произвольного количества символов. Ваша задача дополнить введенную строку до 15 символов в том случае, когда ей не хватает длины. Дополнять ее нужно символом -, ставя его в конец строки. В качестве ответа нужно вывести преобразованную строку
Если поступала на вход строка, у которой уже имелось как минимум 15 символов, то преобразований выполнять никаких не нужно. Выведите строку в том виде, в котором она вводилась
"""
# print(input().ljust(15, '-'))

"""
На вход программе поступает строка. Ваша задача дополнить ее впереди восклицательными знаками так, чтобы длина строки стала 10 символов.
Если на вход поступила строка, длина которой уже превысила 9 символов, то дополнять ее знаками ! не нужно. Просто выведите строку в том виде, в котором она вводилась
"""
# print(input().rjust(10, '!'))

"""
При помощи метода .center дополните введенную строку до 15 символов. В качестве параметра fillchar возьмите нижнее подчеркивание _
"""
# print(input().center(15, '_'))

"""
На вход программе поступает натуральное число, которое не превосходит значение 109
Ваша задача вывести данное число так, чтобы вывод занимал 10 разрядов. Если у числа не хватает разрядов, необходимо добавлять
"""
# print(input().zfill(10))

"""
Вводится строка, которая может быть окружена символами -, _, !, ?
Ваша задача избавиться от символов -, _, !, ? и вывести полученную строку
"""
# print(input().strip('-, _, !, ?'))

"""
Вводится строка, которая может быть окружена символами -, _, !, ?
Ваша задача убрать`все символы -, _, !, ? слева от строки и вывести полученный результат
"""
# print(input().lstrip('-, _, !, ?'))
# print(input().rstrip('-, _, !, ?'))

# экранирование
# s = """hello
# world
# and
# by
# """
# print(s)

"""
Создайте этот прекрасный рисунок
Старайтесь для переноса строк использовать экранированный символ "\n"
"""

# print("/\_/\\\n>^,^<\n / \\\n(|_|)_/")

"""
Смог нарисовать котика, сможешь и песика!)))
"""
# print("  /~~~\\\n //^ ^\\\\\n(/(_*_)\\)\n_/''*''\_\n(/_)^(_\\)")

"""
Напишите программу, которая считывает слово, затем выводит:
«Что Вы сказали? [это слово] ? Какое интересное слово».
"""
# n = input()
# print(f'Что Вы сказали? {n}? Какое интересное слово')

"""
Программа запрашивает у пользователя имя и фамилию, после чего выводит приветственное сообщение в следующем формате «Здравствуйте, <фамилия> <имя>!»
"""
# surname = input()
# name = input()
# print('Здравствуйте, {1} {0}!'.format(surname, name))

# n = int(input())
# print(f'Для числа {n} предыдущим будет число {n-1}.\nДля числа {n} следующим будет число {n+1}.')

"""
Теперь ваша программа спрашивает у пользователя не только имя, но и его возраст. После этого программа должна вывести сообщение:
"Hello <name>. You are <age> years old."
Обратите внимание, что буквы в имени все должны быть заглавные. И не забывайте пользоваться f-строкой
"""
# name = input()
# age = input()
# print(f'Hello {name.upper()}. You are {age} years old.')

"""
Напишите программу, которая запрашивает имя пользователя и его год рождения. 
Программа должна вывести на экран сообщение "<Имя пользователя>, вам исполнится 77 лет в <год>"
"""
# name = input()
# year = int(input())
# print(f'{name}, вам исполнится 77 лет в {year + 77}')

"""
Напишите программу для перевода натурального значения секунд в значение минут определенного формата.
"""
# time = int(input())
# min = time // 60
# sec = time % 60
# print(f'{time} сек - это {min} мин. {sec} сек.')

"""
Вам поступает на вход два натуральных числа - ширина экрана и его высота в пикселях. В результате на экране разрешение экрана и общее количество пикселей в определенном формате. Все знаки препинания, пробелы, регистр букв важны. Также обратите внимание, что в этом месте «1920 x 1080» стоит английская буква «x»
"""
# width, height = map(int,input().split())
# print(f'Разрешение экрана: {width} x {height}.\nОбщее количество пикселей = {width * height}.')

"""
Давайте при помощи F-строк выведем информацию о трех видах деления, которые мы с вами изучили ранее: обычное деление, целочисленное и деление по остатку. 
"""
# first_number = int(input())
# second_number = int(input())
# print(
#     f"{first_number} / {second_number} = {first_number / second_number}\n{first_number} // {second_number} = {first_number // second_number}\n{first_number} % {second_number} = {first_number % second_number}"
# )

"""
Нашей программе поступает на вход x, y, z - три целых числа, обозначающие координаты вектора А. Затем необходимо найти координаты вектора B, путем увеличения на 5 каждой из координаты вектора А.
Оба вектора необходимо распечатать в определенном формате
"""
# x, y, z = int(input()), int(input()), int(input())
# print(f"Vector A({x}, {y}, {z})\nVector B({x+5}, {y+5}, {z+5})")

# dollar_exchange, number_dollars = float(input()), int(input())
# print(f'Current dollar rate is {dollar_exchange}. You want to buy {number_dollars} dollars\nYou must pay {dollar_exchange * number_dollars}')

'''
На вход вашей программе поступают координаты точки x и y - два целых числа, каждое вводится на отдельной строчке. 
Ваша задача обязательно сохранить поступающие на вход значения в переменные x и y соответственно, и затем вывести строку вида Точка(x = {значение}, y = {значение})
'''
# x, y = int(input()), int(input())
# print(f'Точка({x = }, {y = })')

'''
У курсов валют на биржах обычно указываются 4 знака после запятой, как показано на картинке ниже
Но при купле/продаже обычно оставляют только два знака после запятой. В этом и будет заключаться, ваша задача - принять вещественное число, и вывести его в формате двух знаков после запятой
'''
# x = float(input())
# print(f'{x:.2f}')

'''
водится целое число, необходимо вывести его на экран, отведя как минимум 10 разрядов под отображение числа. Если в числе не хватает разрядов, необходимо выводить незначащие нули
'''
# x = int(input())
# print(f'{x:010d}')

'''
Вводится целое число, необходимо выполнить выравнивание его по центру, отведя 15 символов под отображение числа. Символом заполнителем должен являться знак дефиса -
'''
# n = int(input())
# print(f'{n:-^15d}')

# text = input()
# print(f"|{text:&^20}|\n|{text:&>20}|\n|{text:&<20}|")

