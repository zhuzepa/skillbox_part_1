'''
Напишите программу, которая распечатает все натуральные числа кратные 5 от 195 до 6785 включительно в порядке убывания.

Каждое число следует выводить на отдельной строчке как в примере ниже
'''

n = 6790
while n > 195:
    n -= 5
    print(n)