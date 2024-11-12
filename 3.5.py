# A

from sys import stdin
summa = 0
for item in stdin.read().split():
    summa += int(item)
print(summa)

# B

from sys import stdin
delta = 0
strings = [line.rstrip('\n') for line in stdin.readlines()]
for string in strings:
    _, then, now = string.split()
    delta += int(now) - int(then)
print(round(delta / len(strings)))

# C

from sys import stdin
for string in stdin.readlines():
    if string == '\n':
        print(string)
    elif string.strip()[0] != '#':
        if (pos := string.find('# ')) + 1:
            string = string[:pos]
        print(string.strip('\n'))
        
# D

from sys import stdin
lines = stdin.readlines()
subject = lines[-1].strip('\n').lower()
objects = lines[:-1]
for line in objects:
    if line.lower().find(subject) + 1:
        print(line.strip('\n'))
        
# E

from sys import stdin
words = []
strings = stdin.readlines()
for string in strings:
    for word in string.replace('\n', '').split():
        if word.upper() == word.upper()[::-1]:
            words.append(word)

print('\n'.join(sorted(set(words))))

# F

LITER = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}
data, translit_data = '', ''
with open("cyrillic.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        data += line
for i in data:
    if i.upper() in LITER:
        translit_data += LITER[i.upper()].lower().capitalize() if i == i.upper() else LITER[i.upper()].lower()
    else:
        translit_data += i
with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    print(translit_data, file=file_out)
    
# G

name = input()
numbers = []
with open(name, 'r') as f:
    for line in f:
        numbers.extend([int(x) for x in line.split()])
print(len(numbers))
print(len(list(filter(lambda x: x > 0, numbers))))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers), 2))

# H

file_1 = input()
file_2 = input()
file_out = input()
with open(file_1, encoding='UTF-8') as file_in:
    items_1 = set([item for item in file_in.read().split()])
with open(file_2, encoding='UTF-8') as file_in:
    items_2 = set([item for item in file_in.read().split()])
unique = items_1 ^ items_2
with open(file_out, 'w', encoding='UTF-8') as file_name:
    print('\n'.join(sorted(unique)), file=file_name)
    
# I

first_file, second_file = input(), input()
data = []
with open(first_file, 'r') as f:
    for line in f:
        data.append(line.strip().replace('\t', '').split())
data = [i for i in data if any(i)]
with open(second_file, 'w') as g:
    for line in data:
        print(' '.join(line), file=g)
        
# J

file_name = input().strip()
lines = int(input())
with open(file_name, encoding='UTF-8') as file:
    data = [string for string in file.read().split('\n') if string]
print('\n'.join(data[-lines:]))

