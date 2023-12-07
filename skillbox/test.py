# 4.7 Тренажер «Вывод оповещения»

# your_wallet = int(input('Сколько у вас денег? '))
#
# course_price = 75000
#
# if your_wallet >= course_price:
#     your_wallet -= course_price
#     print("Курс успешно приобретён!")
# else:
#     print("Не хватает денег на счёте")
#
# print("Хорошего дня!")

# 4.8 Тренажер «Проверка суммы»
# first_number = 10
# second_number = 210
# sum_number = 30
#
#
# result_sum = first_number + second_number
#
# if result_sum == sum_number:
#     print('Ответ верный!')
# else:
#     print('Ответ неверный!')
#     print(f'Правильный результат: {result_sum}')

# 4.9 Тренажер «Оператор else в сравнениях»
# sons_number = int(input('Ввежите число: '))
# dad_number = 5
#
# if sons_number == dad_number:
#     print('Угадал!')
# else:
#     print('Не угадал!')
# print('Конец игры')

# a = int(input('Введите число 1: '))
# b = int(input('Введите число 2: '))
# c = int(input('Введите число 3: '))
# if a > b:
#     maximum = a
# else:
#     maximum = b
# if c > maximum:
#     maximum = c
#
# print(f'макс число: {maximum}')

# Вложенные условия

# bank = int(input('Сколько на счету денег? '))
# if bank > 75000:
#     bank -= 75000
#     print('Курс успешно приобритен')
#     if bank < 5000:
#         bank += 1000
#         print('Применили скидку и подарили вам 1000')
# else:
#     print('Денег не хватает на счету')
# print(f'Остаток по счет: {bank}')
# print('Хорошего дня!')

# product = int(input('Введите сумму чека: '))
# delivery = int(input('Введите сумму доставки: '))
# discount = 0
# if product > 10000:
#     print('Хороший чек! Доставка будет снижена вдвое')
#     delivery /= 2
#     if product % 2 == 0:
#         print('Покупателю положен подарок')
#         discount = 500
# price = product + delivery - discount
# print('Полная стоимость товаров: ', price)

# 5.3 Тренажёр «Независимые сравнения»
# x = 1
# y = 5
#
# if x == y:
#     print("X равен Y")
# if x > y:
#     print("X больше Y")
# if x < y:
#     print("X меньше Y")

# 5.4 Тренажёр «Усложнённый расчёт скидки»

# your_wallet = int(input('Введите число:'))
# course_price = 75000
#
# if your_wallet >= course_price:
#     your_wallet -= course_price
#     if your_wallet < 5000:
#         your_wallet += 1000
#         print('Сделана скидка')
#     print('Курс успешно приобретён!')
#
# else:
#     print('Не хватает денег на счету')
#
# print(f'Остаток на счету: {your_wallet}')
# print('Хорошего дня!')

# money = int(input('Введите кол-во полученных денеге: '))
# cheese_price = 60
# ice_cream_price = 20
# if money >= cheese_price:
#     print('На сыр денег хватило')
#     money -= cheese_price
#     if money >= ice_cream_price:
#         print('И на мороженое тоже!')
#         money -= ice_cream_price
#     else:
#         print('Денег маловато')
# else:
#     print('Денег не хватило даже на сыр!')

# profit = int(input('Введите размер прибыли: '))
if profit < 10000:
    tax = profit * 13 / 100
    print('Размер налога (13%) равен: ', tax)
elif profit < 50000:
    tax = profit * 20 / 100
    print('Размер налога (20%) равен: ', tax)
else:
    tax = profit * 30 / 100
    print('Размер налога (30%) равен: ', tax)

# 5.7 Тренажёр «Зависимые сравнения»
x = 1
y = 5

if x > y:
    print('X больше Y')
elif x < y:
    print('X меньше Y')
else:
    print('X равен Y')

