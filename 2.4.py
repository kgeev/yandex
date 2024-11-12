# A

d = int(input())
for i in range(d):
    for j in range(d):
        print((i + 1) * (j + 1), end=' ')
    print()
    
# B

d = int(input())
for i in range(1, d + 1):
    for j in range(1, d + 1):
        print(f'{j} * {i} = {i * j}')

# C

finish = int(input())
limit = 1
current = 0
for pos in range(finish):
    current += 1
    print(pos + 1, end=' ')
    if current == limit:
        print()
        limit += 1
        current = 0
        
# D

d = int(input())
s = 0
for _ in range(d):
    n = int(input())
    while n > 0:
        s += n % 10
        n //= 10
print(s)

# E

n = int(input())
z = 0
for _ in range(n):
    counted = False
    while (s := input()) != 'ВСЁ':
        if s == 'зайка' and counted is False:
            z += 1
            counted = True
print(z)

# F

a = int(input())
b = int(input())
for i in range(a - 1):
    n = int(input())
    while n != 0 and b != 0:
        if n >= b:
            n %= b
        else:
            b %= n
    b = b + n
print(b)

# G

a = int(input())
b = 3
for number in range(a):
    for delay in range(b + number, 0, -1):
        print(f'До старта {delay} секунд(ы)')
    print(f'Старт {number + 1}!!!')
    
# H

count = int(input())
best_name = ''
best_sum = 0
for i in range(count):
    name = input()
    number = int(input())
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    if summa >= best_sum:
        best_sum = summa
        best_name = name
print(best_name)

# I

count = int(input())
result = 0
for _ in range(count):
    number = int(input())
    maximum = -1
    while number > 0:
        if number % 10 > maximum:
            maximum = number % 10
        number //= 10
    result = result * 10 + maximum
print(result)

# J

slices = int(input())
print('А Б В')
for a in range(1, slices + 1):
    for b in range(1, slices + 1):
        for c in range(1, slices + 1):
            if a + b + c == slices:
                print(a, b, c)
                