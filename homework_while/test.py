# n = 6
# total = 0
#
# while n:
#     print(f'process n {n}')
#     total += n
#     n -= 1
# print(total)


# n = 6
# total = 0
#
# while n:
#     print(f'process n {n}')
#     if n < 4:
#         break
#     total += n
#     n -= 1
# print(total)


# number = 123456
# nums_total = 0
#
# while number:
#     remainder = number % 10
#     if remainder < 4:
#         break
#     nums_total += remainder
#     number //= 10
# print(f'nums_total {nums_total}')
# print(number)


# memory = None
#
# while True:
#     command = input('Command: ')
#     if command == 'r':
#         print(f'Memory {memory}')
#     elif command == 'w':
#         memory = input('Помнить: ')
#     elif command == 'q':
#         break
#     else:
#         print('знать команды r,w,q')


cash = int(input('Сколько мне платят ЗП: '))

if cash >= 230000:
    print('Делаем красивую работу')
else:
    print('Открывается вакансия на HH')
