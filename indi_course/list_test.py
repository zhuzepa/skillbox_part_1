'''
Сохраните в переменной  my_list список, в котором должно быть 77 элемента и все они представляют собой единицу
'''
# my_list = []
# for i in range(77):
#     my_list.append(1)
# print(my_list)

# my_list = [1] * 77
# print(my_list)

'''
Сохраните в переменной  my_list список из 15-ти повторений букв q, w, t
В качестве ответа выведите на экран переменную my_list
'''
# my_list = ['q', 'w', 't'] * 15
# print(my_list)

'''
Программа получает на вход список из целых чисел. Ваша задача вывести True в случае, если в данном списке встречается значение 777. В противном случае вывести False
'''

# my_list = list(map(int, input().split()))
# print(sum(my_list))

'''
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
'''

# my_list = list(map(int, input().split()))
# print(min(my_list), max(my_list))

'''
Программа получает на вход список из целых чисел. Ваша задача найти среднее арифметическое введенного списка чисел
'''
# my_list = list(map(int, input().split()))
# print(sum(my_list) / len(my_list))

# Списки: индексы и срезы

'''
Программа получает на вход список целых чисел и ваша задача вывести второй элемент этого списка.
Гарантируется, что список будет состоять не менее чем из трех элементов
'''

# my_list = list(map(int, input().split()))
# print(my_list[1])

'''
Программа получает на вход список целых чисел и ваша задача вывести срез списка с третьего элемента по пятый включительно.
Гарантируется, что список будет состоять не менее чем из пяти элементов.
'''
# my_list = list(map(int, input().split()))
# print(my_list[2:5])

'''
Программа получает на вход список целых чисел и ваша задача вывести последние три элемента этого списка через срез
Гарантируется, что список будет состоять не менее чем из пяти элементов.
'''
# my_list = list(map(int, input().split()))
# print(my_list[-3:])

'''
Программа получает на вход список целых чисел и ваша задача вывести каждый третий элемент этого списка, начиная со второго по счету значения.
'''
# my_list = list(map(int, input().split()))
# print(my_list[1::3])

'''
Программа получает на вход список целых чисел и ваша задача вывести этот список  в обратном порядке при помощи срезов
Гарантируется, что список будет состоять не менее чем из  трех элементов.
'''
# my_list = list(map(int, input().split()))
# print(my_list[::-1])

'''
Перед вами список топовых сериалов по версии кинопоиска. Ваша задача заменить в нем сериал "Бригада" на "Сверхъестественное" и "Друзья" на "Настоящий детектив"
'''
# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# top[-1], top[-5] = 'Сверхъестественное', 'Настоящий детектив'
#
# print(top)

'''
Перед вами находится список months, хранящий сокращенное название месяцев в году
Ваша программа получает на вход порядковый номер месяца в году - целое число от 1 до 12.
Ваша задача распечатать кратное название месяца, которое соответствует порядковому номеру месяца
'''
# a = int(input())
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# print(months[a-1])

'''
В вашем распоряжении список numbers. Ваша задача добавить по порядку четыре следующих элемента в конец списка: 111, 222, 789 и 201
В качестве ответа необходимо вывести измененный список numbers
'''

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.append(111), numbers.append(222), numbers.append(789), numbers.append(201)
# print(numbers)

'''
В вашем распоряжении список numbers. Ваша задача выполнить четыре следующих действия в том же порядке, как они указаны в списке:
добавить значение 111  на 5-й индекс;
добавить значение 222  на 8-й индекс;
добавить значение 789  на 0-й индекс;
добавить значение 201  на 11-й индекс;
В качестве ответа необходимо вывести измененный список numbers
'''
# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.insert(5, 111), numbers.insert(8, 222), numbers.insert(0, 789), numbers.insert(11, 201)
# print(numbers)

'''
В вашем распоряжении два списка numbers  и extra. Ваша задача расширить numbers список за счет списка extra
Все элементы списка extra должны добавиться по порядку в конец списка numbers
В качестве ответа необходимо вывести измененный список numbers
'''
# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
#
# extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]
# numbers.extend(extra)
# print(numbers)

'''
В вашем распоряжении список numbers. Ваша задача выполнить действия из списка строго в том же порядке, а именно:
удалить элемент, стоящий на последней позиции;
удалить элемент, стоящий на 0-й позиции;
удалить элемент, стоящий на 12-й позиции;
удалить элемент, стоящий на 7-й позиции;
В качестве ответа необходимо вывести на первой строке измененный список numbers, а на второй - сумму значений удаленных элементов
'''

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# del_index = numbers.pop(-1), numbers.pop(0), numbers.pop(12), numbers.pop(7)
# print(numbers)
# print(sum(del_index))

'''
Метод remove
В вашем распоряжении список numbers.Ваша задача удалить из этого списка числа 3, 5, 7 и 9. 
 В качестве ответа необходимо вывести измененный список numbers
'''
# numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
# list(map(numbers.remove, (3, 5, 7, 9)))
# print(numbers)

'''
В вашем распоряжении список numbers. Ваша задача отсортировать список numbers в порядке убывания  и вывести на экран результат.
'''
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.sort(reverse=True)
print(numbers)