#print('ДА' if input() == 'Python' else 'НЕТ')


'''
Во всех странах присутствует подоходный налог. В каких-то странах он больше, в каких-то меньше. В РФ граждане платят подоходный налог в размере 13%.
Представьте теперь, что люди с доходом меньше 20000 рублей освобождены от уплаты налога. Напишите программу, которая получает на вход значение дохода в виде целого числа и выводит на экран сумму, оставшуюся после уплаты налога в 13%. Если у человека зарплата меньше 20000р налог не удерживается.
'''
# a = int(input())
# if a > 20000:
#     a -= a * 13 / 100
#
# print(a)

'''
Вводятся два целых числа, каждое в отдельной строке.
Ваша задача вывести наибольшее из данных чисел.
Примечание: используйте только условный оператор, функцией max пользоваться нельзя
'''
# a, b = int(input()), int(input())
# if a > b:
#     print(a)
# else:
#     print(b)
'''
Программа получает на вход три натуральных числа A, B и C через пробел. 
Вам необходимо вывести YES в том случае, если A + B = C и вывести NO в противном случае.
'''
# a, b, c = map(int, input().split())
# if a + b == c:
#     print('YES')
# else:
#     print('NO')

'''
Программа получает на вход список из целых чисел, при этом гарантируется, что числа в списке повторяться не будут.
​​Ваша задача удалить из этого списка числа 3, 5, 7 и 9. 
Обратите внимание, что каждое из чисел 3, 5, 7 и 9. необязательно должно присутствовать в введенном списке.
В качестве ответа необходимо распечатать измененный список
Примечание:
Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку
'''

# a = list(map(int, input().split()))
# if 3 in a:
#     a.remove(3)
# if 5 in a:
#     a.remove(5)
# if 7 in a:
#     a.remove(7)
# if 9 in a:
#     a.remove(9)
# print(a)


'''
На момент написания текста из РФ можно было вывозить не более 10000$ или эквивалент в другой валюте. При превышении этой суммы необходимо составлять декларацию.
Давайте представим, что сумму выше 10000 долларов таможня забирает себе и вам останется только 10000$.
Давайте напишем такую программу, которая будет принимать целое положительное число - сумма в долларах. Если она не превышает 10000$, то выводим текст Сумма <значение> не превышает лимит, проходите
Если сумма превышает 10000$ выводим текст Ого! <значение>! Куда вам столько? Мы заберем <разница>
И конечно же нужно использовать сами знаете кого, иначе ваше решение не пройдет
'''


# if (a := int(input())) <= 10000:
#     print(f'Сумма {a} не превышает лимит, проходите')
# else:
#     b = a - 10000
#     print(f'Ого! {a}! Куда вам столько? Мы заберем {b}')

'''
На вход вашей программе поступает фраза, если в ней присутствует слово walrus выводим текст Нашли моржа, иначе выводим Никаких моржей тут нет.
И конечно же нужно использовать сами знаете кого, иначе ваше решение не пройдет
'''
# if 'walrus' in (a := input()):
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

'''
Программа принимает на вход два слова s и t. 
Если слово t является словом s, записанным наоборот, выведите YES, иначе выведите NO.
Слова состоят из маленьких латинских букв. Входные данные не содержат лишних пробелов. Слова непустые, и их длины не превосходят 100 символов.
'''
# s, t = input(), input()
# if t == s[::-1]:
#     print('YES')
# else:
#     print('NO')

'''
Требуется написать программу, определяющую, является ли четырехзначное натуральное число N палиндромом, т.е. числом, которое одинаково читается слева направо и справа налево.
Программа получает на вход целое положительное четырехзначное число N  и должна вывести YES,  если число N является палиндромом, и NO - если не палиндром.
'''
# a = int(input())
# a = str(a)
#
# if a == a[::-1]:
#     print('YES')
# else:
#     print('NO')

'''
Даны три натуральных числа a, b, c записанные в отдельных строках. Ваша задача определить, существует ли треугольник с такими сторонами. 
Для этого вспоминаем теорему о существовании треугольника. Она утверждает, что треугольник существует, если сумма любых двух сторон больше оставшейся третьей.
Выведите строку YES, если условие теоремы выполняется, иначе выведите строку NO.
'''
# a, b, c = int(input()), int(input()), int(input())
# if a + c > b and a + b > c and c + b > a:
#     print('YES')
# else:
#     print('NO')
#


'''
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером (иногда и с незначащими нулями), где сумма первых трех цифр равна сумме последних трех. Т.е. билеты с номерами 385916 и 2011 – счастливые, т.к. 3+8+5=9+1+6 и 0+0+2=0+1+1. Вам требуется написать программу, которая проверяет «счастливость» билета.

Программа получает на вход одно целое число N (0 ≤ N < 106) и должна вывести «YES», если билет с номером N счастливый и «NO» в противном случае.
'''
# x = int(input())
# d6 = x % 10
# d5 = x // 10 % 10
# d4 = x // 100 % 10
# d3 = x // 1000 % 10
# d2 = x // 10000 % 10
# d1 = x // 100000
#
# if d1+d2+d3 == d4+d5+d6:
#     print('YES')
# else:
#     print('NO')

'''
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том, являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.
'''
