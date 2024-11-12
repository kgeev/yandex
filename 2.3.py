# A

while (s := input()) != 'Три!':
    print('Режим ожидания...')
print('Ёлочка, гори!')

# B

count = 0

while (s := input()) != 'Приехали!':
    if 'зайка' in s:
        count += 1
print(count)


# C

k = int(input())
n = int(input())
for i in range(k, n + 1):
    print(i, end=' ')
    
# D

k = int(input())
n = int(input())
if n >= k:
    for i in range(k, n + 1):
        print(i, end=' ')
else:
    for i in range(k, n - 1, - 1):
        print(i, end=" ")
        
# E

summa = 0

while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
    summa += price

print(summa)

# F

a, b = int(input()), int(input())

while a != 0 and b != 0:
    if a >= b:
        a %= b
    else:
        b %= a

print(a + b)

# G

a, b = a1, b1 = int(input()), int(input())

while a != 0:
    a, b = b % a, a

print(a1 * b1 // (a + b))

# H

k = input()
n = int(input())
for i in range(n):
    print(k)
    
# I

num = int(input())

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)

# J

x, y = 0, 0

while (direction := input()) != 'СТОП':
    n = int(input())
    if direction == 'ВОСТОК':
        x += n
    elif direction == 'ЗАПАД':
        x -= n
    elif direction == 'СЕВЕР':
        y += n
    elif direction == 'ЮГ':
        y -= n
        
print(y)
print(x)

# K

num = int(input())
summa = 0
while num > 0:
    summa += num % 10
    num //= 10
print(summa)

# L

num = int(input())
maximum = -1
while num > 0:
    maximum = max(maximum, num % 10)
    num = num // 10
print(maximum)

# M

count = int(input())

first = ''

for _ in range(count):
    name = input()
    if first == '':
        first = name
    elif name < first:
        first = name

print(first)
