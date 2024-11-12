# A

name = input()
print("Как Вас зовут?")
print(f'Здравствуйте, {name}!')
print("Как дела?")
gb = input()
if (gb == "хорошо"):
    print("Я за вас рада!")
elif (gb == "плохо"):
    print("Всё наладится!")
    
# B

pet = int(input()) 
vas = int(input()) 
if pet > vas:
    print("Петя")
else:
    print("Вася")
    
# C

pet = int(input()) 
vas = int(input()) 
tol = int(input()) 
if (pet > vas > tol) or (pet > tol > vas):
    print("Петя")
elif (vas > pet > tol) or (vas > tol > pet):
    print("Вася")
else:
    print("Толя")
    
# D

pet = int(input()) 
vas = int(input()) 
tol = int(input())
p = str("Петя")
v = str("Вася")
t = str("Толя") 
if (pet > vas > tol):
    print(f'1. {p}')
    print(f'2. {v}')
    print(f'3. {t}')
elif (pet > tol > vas):
    print(f'1. {p}')
    print(f'2. {t}')
    print(f'3. {v}')
elif (vas > pet > tol):
    print(f'1. {v}')
    print(f'2. {p}')
    print(f'3. {t}')
elif (vas > tol > pet):
    print(f'1. {v}')
    print(f'2. {t}')
    print(f'3. {p}')
elif (tol > pet > vas):
    print(f'1. {t}')
    print(f'2. {p}')
    print(f'3. {v}')
elif (tol > vas > pet):
    print(f'1. {t}')
    print(f'2. {v}')
    print(f'3. {p}')
    
# E

p = int(input()) 
v = int(input()) 
if p > v:
    print("Петя")
else:
    print("Вася")
    
# F

n = int(input())
if (n % 4 == 0) and (n % 100 != 0):
    print("YES")
elif (n % 100 == 0) and (n % 400 == 0):
    print("YES")
else:
    print("NO")
    
# G

n = int(input())
if n // 1000 == n % 10 and n // 100 % 10 == n // 10 % 10:
    print("YES")
else:
    print("NO")
    
# H

text = input()
if "зайка" in text:
    print("YES")
else:
    print("NO")
    
# I

a = input()
b = input()
c = input()

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)
    
# J

n = int(input())
s1 = n // 10 // 10 + n // 10 % 10
s2 = n % 100 // 10 + n % 100 % 10
if s1 < s2:
    print(str(s2) + str(s1))
else:
    print(str(s1) + str(s2))
    
# K

n = int(input())
n3 = n % 10
n2 = n // 10 % 10
n1 = n // 100
if n1 < n2 < n3 and n3 + n1 == 2 * n2:
    print("YES")
elif n1 < n3 < n2 and n2 + n1 == 2 * n3:
    print("YES")
elif n2 < n1 < n3 and n2 + n3 == 2 * n1:
    print("YES")
elif n2 < n3 < n1 and n2 + n1 == 2 * n3:
    print("YES")
elif n3 < n1 < n2 and n2 + n3 == 2 * n1:
    print("YES")
elif n3 < n2 < n1 and n1 + n3 == 2 * n2:
    print("YES")
else:
    print("NO")
    
# L

a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
    
# M

a = int(input())
b = int(input())
c = int(input())
if a // 10 == b // 10 == c // 10:
    print(a // 10)
elif a % 10 == b % 10 == c % 10:
    print(a % 10)
else:
    print("NO")
    
# N

n = int(input())
f = n // 100
s = n // 10 % 10
t = n % 10
mid = f + s + t - min(f, s, t) - max(f, s, t)
if min(f, s, t) != 0:
    minimal = min(f, s, t) * 10 + mid
elif mid != 0:
    minimal = mid * 10
else:
    minimal = max(f, s, t) * 10
maximal = max(f, s, t) * 10 + mid
print(minimal, maximal)

# O

a = int(input())
b = int(input())
a1 = a // 10
a2 = a % 10
b1 = b // 10
b2 = b % 10
maxim = max(a1, a2, b1, b2)
minim = min(a1, a2, b1, b2)
mm = (a1 + a2 + b1 + b2 - maxim - minim) % 10
print(maxim * 100 + mm * 10 + minim)

# P

p = int(input())
v = int(input())
t = int(input())
first = max(p, v, t)
third = min(p, v, t)
second = p + v + t - first - third
if first == p:
    first_name = 'Петя'
elif first == v:
    first_name = 'Вася'
else:
    first_name = 'Толя'
if second == p:
    second_name = 'Петя'
elif second == v:
    second_name = 'Вася'
else:
    second_name = 'Толя'
if third == p:
    third_name = 'Петя'
elif third == v:
    third_name = 'Вася'
else:
    third_name = 'Толя'
print(f'{first_name: ^24}')
print(f'{second_name: ^8}{" ": ^16}')
print(f'{" ": ^16}{third_name: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')

# Q

a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print('Infinite solutions')
elif a == 0 and b != 0 and c != 0:
    print(f'{-(c / b):.2f}')
elif a == b == 0:
    print('No solution')
elif a == c == 0:
    print(0)
else:
    disc = (b ** 2) - (4 * a * c)
    if disc == 0:
        print(f'{(-b) / (2 * a):.2f}')
    elif disc > 0:
        x1 = (-b - (disc ** 0.5)) / (2 * a)
        x2 = (-b + (disc ** 0.5)) / (2 * a)
        print(f'{min(x1, x2):.2f} {max(x1, x2):.2f}')
    else:
        print('No solution')
        
# R

a = int(input())
b = int(input())
c = int(input())
maxim = max(a, b, c)
minim = min(a, b, c)
mm = (a + b + c) - maxim - minim
if (maxim ** 2) < (mm ** 2) + (minim ** 2):
    print("крайне мала")
elif (maxim ** 2) == (mm ** 2) + (minim ** 2):
    print("100%")
elif (maxim ** 2) > (mm ** 2) + (minim ** 2):
    print("велика")
    
# S

x = float(input())
y = float(input()) 

if (x ** 2 + y ** 2) ** 0.5 > 10:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -4 <= x < 0 and 0 <= y <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -7 <= x < -4 and 0 <= y <= 5 and (5 * x - 3 * y) > -35:
    print('Опасность! Покиньте зону как можно скорее!')
elif (0.25 * x ** 2 + 0.5 * x - 9) <= y <= 0:
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')
    
# T

nature1 = input()
nature2 = input()
nature3 = input()

nature = ''

if 'зайка' in nature1:
    nature = nature1
if 'зайка' in nature2:
    if nature == '' or nature > nature2:
        nature = nature2
if 'зайка' in nature3:
    if nature == '' or nature > nature3:
        nature = nature3

print(nature, len(nature))
