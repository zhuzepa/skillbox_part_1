# print(1, 2, 3, sep='/')
# print(3, 4, end='--')
# print(666)

# a, b, c = map(int, input().split())
# print(a, b, c, sep=',')

# a = int(input())
# print(a - 1, a, a + 1, sep='<')

# a = input()
# print(a, end=' - Сказала она!')

# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# print('Основатель', 'Питона', sep='_', end='!')

# a, b, c = map(int, input().split())
# print(a+b+c)

# Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа
a = int(input())
b = a % 10
c = a % 100 // 10
d = a % 1000 // 100
print(b + c + d)

# Выиграть в лотерею