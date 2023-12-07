# ''' Задача 1. Циклы — это сложно?
#  Даша начала проходить циклы. Она написала программу, которая просто должна считать сумму чисел до тех пор, пока мы не ввели 0,
#  но что-то пошло не так.
# '''
# number = int(input("Введите число: "))
# total = 0
# while number != 0:
#     total += number
#     number = int(input("Введите число: "))
# print(total)
#
# '''
# Задача 2. Закономерности
#
# Арина считает, что всё в нашей жизни закономерно. И она в очередной раз убедилась в этом, когда узнала своё домашнее задание по математике.
#
# Напишите программу, которая выводит на экран вот такую последовательность чисел (каждое число в новой строчке):
# '''
#
# counter = 0
# while counter != 98:
#     counter += 7
#     print(counter)
#
#
#
# Цель задания
# Потренироваться в работе с циклом while и оператором break.
#
# Что нужно сделать
# Задача 1. Бегать — это полезно
#
# Представим, что у нас далёкое будущее и мы можем заниматься спортом на планетах
# со странными перепадами температур. Спортсмен бегает по стадиону до тех пор,
# пока температура на улице больше 15 градусов. Он пробегает 20 метров,
# затем температура падает на два градуса,
# и, если уже в этот момент она стала меньше
# либо равна 15 градусам, спорт сразу заканчивается.
# Если же всё в порядке, то он проходит пешком ещё 10 метров. Затем всё это повторяется.
#
# Напишите программу, которая спрашивает у пользователя, сколько на улице градусов, и, исходя из погоды, считает количество пройденных по стадиону метров и выводит ответ на экран.

outdoor_temperature = int(input('Какая температура на улице: '))
run = 0
while outdoor_temperature >= 15:
    run += 20
    outdoor_temperature -= 2
    if outdoor_temperature <= 15:
        break
    run += 10
#
# print(run)

'''
Задача 2. Расшифровка кода
Нам нужно расшифровать определённый код в виде одного большого числа. Для этого нужно посчитать сумму цифр справа налево.
Если мы встречаем в числе цифру 5, то выводим сообщение «Обнаружен разрыв» и заканчиваем считать сумму.
В конце программы на экран выводится сумма тех цифр, которые мы взяли.
'''

# large_number = 73753323549
# total_num = 0
# while large_number:
#     remainder = large_number % 10
#     large_number //= 10
#     if remainder == 5:
#         break
#
#
#
# print('обнаружен разрыв')
# print(total_num)

'''
Задача 3. Начальная школа

Авторы учебника по математике для второклассников очень любят всё усложнять. 
Например, отрицательные числа изучают только в пятом классе, а они всё норовят дать задачки на них во втором классе.
Нам нужна программа, которая будет проверять, что в учебнике для второклашек не будет отрицательных чисел.

Напишите программу, которая считывает числа до тех пор, пока не встретит отрицательное число. 
При появлении отрицательного числа программа завершается и показывает количество введенных чисел. 
Подумайте, обязательно ли здесь использовать оператор break.
'''
# quantity = 10
# count_quantity = 0
# while quantity:
#     quantity -= 1
#     if quantity <= 0:
#         break
#     count_quantity += quantity
#
# print(f'сумма {count_quantity}')
# print('Обнаружено отрицательное число')


# count_quantity = 0
# while True:
#     quantity = int(input('Введите число: '))
#     if quantity < 0:
#         print('Обнаружено отрицательное число')
#         break
#     count_quantity += 1
#
# print(f'Сумма: {count_quantity}')
#
# Из дз:
# current_number = 0
# count = 0
# while True:
#     current_number = int(input("Введите число: "))
#     if current_number < 0:
#         print("Найдено отрицательное число!")
#         print("Введённых чисел, не учитывая отрицательное = ", count)
#         break
#     count += 1
#
#

'''
Задача 4. Ставки приняты, ставок больше нет

Костя опять за старое! Только теперь он играет в кубики более надёжно, то есть на какую-то фиксированную сумму.
 И при этом пока что постоянно выигрывает!
Однако по правилам это не мешает ему проиграть сразу всё.

Напишите программу, которая запрашивает у пользователя начальное количество денег и, пока оно меньше 10 000,
запрашивает число, которое выпало на кубике (от 1 до 6). Если на кубике выпало 3,
то выводится сообщение «Вы проиграли всё!», и деньги обнуляются. Если выпало другое число, к сумме прибавляется 500.
'''

# how_much_money = int(input('Сколько всего денег: '))
# while how_much_money < 10000:
#     number_cube = int(input('Введите число от 1 до 6: '))
#     if number_cube == 3:
#         how_much_money = 0
#         print(f'Вы проиграли всё!, ваш баланс = {how_much_money}')
#         break
#     how_much_money += 500
#     print(how_much_money)
#
# else:
#     print('Сумма меньше 10 000, играть нельзя')

'''
Задача 1. Неправильный таймер

Петя писал таймер для телефона, но у него что-то пошло не так.
Скопируйте программу в редактор, исправьте ошибки и убедитесь, что на экран выводятся числа с 10 до 0 и сообщение «Время вышло!».
'''
#
# count = 0
# while count <= 10:
#     count += 1
#     print(count)
#     if count == 0:
#         break
#
# else:
#     print('Время вышло!')
#
#
#
# count = 10
# while count >= 0:
#     print(count)
#     if count == 0:
#         print('Время вышло!')
#     count -= 1
#
# # Это не единственный вариант решения, их может быть несколько, например
#
# count = 10
# while count + 1:
#     print(count)
#     count -= 1
# print('Время вышло!')
'''
Задача 2. Тестируем приложение

Напишите программу, которая имитирует работу с приложением: программа спрашивает у пользователя «Продолжаем работать?
1/0: » до тех пор, пока пользователь не введёт 0, — после этого выводится сообщение: «Приложение закрывается…».
В конце программы также выводится сообщение: «Работа завершена».
Для создания бесконечного цикла используйте while True. 
'''


# while True:
#     continio = int(input('Продолжаем работать? 1/0: '))
#     if continio == 1:
#         continue
#     print('Приложение закрывается')
#     break
#
# print('Работа завершена')

'''
Задача 3. Вирус

Дима написал программу-вирус специально для того, чтобы проучить своего друга-должника, который никак не хочет возвращать скейтборд.
Программа не даёт работать за компьютером и постоянно выводит на экран сообщение “Компьютер заблокирован. 
Вернёшь скейт - скажу код разблокировки!”. Как только вводится правильный код: вирус удаляется.
Напишите такую же программу, которую написал Дима. Код не может начинаться с цифры 0.
'''
# codee = 555
#
# while True:
#     print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
#     type_code = int(input('Введите код: '))
#     if type_code == 0:
#         print('Код не может начинаться с цифры 0.')
#
#     if type_code == codee:
#         print('Код верный, завершаю работу...')
#         break

'''
Задача 1. Надоедливый заказчик

Нашему заказчику нужно, чтобы фраза «Я — программист!» выводилась на экран столько раз, сколько он сам этого захочет.

Напишите программу, которая запрашивает число — количество строчек 
с фразой «Я — программист!» — и столько же раз выводит на экран эту фразу. 
Для решения задачи используйте переменную-счётчик.
'''
# count = int(input('Сколько раз вывести фразу Я — программист: '))
# while count > 0:
#   print('Я — программист')
#   count -= 1


'''
Задача 2. Напоминалка

У Евгения много работы, а ещё он очень забывчивый. Иногда он забывает о какой-нибудь важной встрече, 
и ему приходится выслушивать критику от начальства. Напишите для него программу-напоминалку. 
В самом начале программа спрашивает, сколько раз ему напомнить, а затем нужное количество раз выводит: «Вы хотели не забыть о чём-то». 
'''

# reminder = int(input('Сколько раз напомнить: '))
# while reminder:
#     reminder -= 1
#     print('«Вы хотели не забыть о чём-то»')
#



'''
Задача 3. Рыбалка

Наши прекрасные родственники удачно сходили на рыбалку. Настолько, что ходили мешком перетаскивать рыбу с берега в машину целых n раз. Каждый мешок они взвешивали на электронных весах (все мешки весили по-разному). Напишите программу для весов, которая считает суммарный вес мешков и выводит его на экран. 
'''