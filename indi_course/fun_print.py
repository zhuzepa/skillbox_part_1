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
# a = int(input())
# b = a % 10
# c = a % 100 // 10
# d = a % 1000 // 100
# print(b + c + d)

# Выиграть в лотерею

# n = int(input())
# k_100 = n // 100
# n = n % 100
# k_20 = n // 20
# n = n % 20
# k_10 = n // 10
# n = n % 10
# k_5 = n // 5
# n = n % 5
# print(k_100+k_20+k_10+k_5+n)
#
#
# n = int(input())
# k_100 = n // 100
# n = n % 100
# k_20 = n // 20
# n = n % 20
# k_10 = n // 10
# n = n % 10
# k_5 = n // 5
# n = n % 5
# print(k_100 + k_20 +k_10 + k_5 + n)

# Электронныечасы - 1
# n = int(input())
# n = n % 1440
# print(n // 60, n % 60)
#
# n = int(input())
# print(n // 60 % 24, n % 60)

# Следующее четное
# n = int(input())
# print((n // 2 + 1) * 2)

# print((4 // 2 + 1) * 2)
# print((1 // 2 + 1) * 2)
# print(1 // 2)
# print(1 * 2)


# Электронные часы - 2
n = int(input())
hour = (n // 3600) % 24
n = n % 3600
minute = n // 60
n = n % 60
sec = n
print(hour, ':', minute // 10, minute % 10, ':', sec // 10, sec % 10, sep='')
