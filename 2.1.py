2.1
# A

print("Привет, Яндекс!")

# B

name = input()
print("Как Вас зовут?")
print("Привет,", name)

# C
phrase = input()
print(phrase)
print(phrase)
print(phrase)

# D

cash = int(input())
priсe = int(38 * 2.5)
print(cash - priсe)

# E

price = int(input())
weight = int(input())
cash = int(input())
print(cash - (price * weight))

# F

name = input()
price = int(input()) 
weight = int(input())
cash = int(input())
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {price * weight}руб")
print(f"Внесено: {cash}руб")
print(f"Сдача: {cash - price * weight}руб")

# G

n = int(input())
print('Купи слона!\n' * n)

# H

N = int(input()) 
str = input()
print(f'Я больше никогда не буду писать "{str}"!\n' * N)

# I

n = int(input()) 
m = int(input()) 
print(int(n * m / 2))

# J

name = input()
nh = int(input()) 
group = nh // 100
nc = nh % 10
bed = nh // 10 % 10
print(f'Группа №{group}.')
print(f'{nc}. {name}.')
print(f'Шкафчик: {nh}.')
print(f'Кроватка: {bed}.')

# K

n = int(input()) 
a = n // 1000 % 10
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
print(f'{b}{a}{d}{c}')

# L

n = int(input()) 
m = int(input())  
a = n // 100
b = n // 10 % 10
c = n % 10
a2 = m // 100
b2 = m // 10 % 10
c2 = m % 10
a3 = (a + a2) % 10
b3 = (b + b2) % 10
c3 = (c + c2) % 10
print(f'{a3}{b3}{c3}')

# M

n = int(input()) 
m = int(input()) 
print(m // n)
print(m % n)

# N

n = int(input()) 
m = int(input()) 
z = int(input())
print(n + z + 1)

# O

N = int(input()) 
M = int(input()) 
T = int(input())
M2 = M + T
N2 = (N + M2 // 60) % 24
M3 = M2 % 60
print(f'{N2:02d}:{M3:02d}')

# P

A = int(input()) 
B = int(input()) 
C = int(input())
rs = B - A
print(f'{rs / C:.2f}')

# Q

A = int(input()) 
B = int(input(), 2)
print(f'{A + B}')

# R

A = int(input(), 2)
B = int(input()) 
print(f'{B - A}')

# S

name = input()
price = int(input()) 
weight = int(input())
cash = int(input())
ves_zen = str(f'{weight}кг * {price}руб/кг')
cash2 = str(f'{cash}руб')
sdaha = str(f"{cash - price * weight}руб")
itogo = str(f'{price * weight}руб')
print("================Чек================")
print(f'Товар: {name:>28}')
print(f'Цена: {ves_zen:>29}')
print(f'Итого: {itogo:>28}')
print(f"Внесено: {cash2:>26}")
print(f"Сдача: {sdaha:>28}")
print("===================================")

# T

N = int(input()) 
M = int(input())
K1 = int(input())
K2 = int(input())
weight_1 = int((M - K2) * N / (K1 - K2))
weight_2 = int(N - weight_1)
print(f'{weight_1} {weight_2}')


