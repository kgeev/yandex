# A

def print_hello(name):
    print(f'Hello, {name}!')   
    
# B

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# C

def number_length(number):
    return len(str(abs(number)))

# D

def month(number, language):
    MONTH = {
        'en': [
            'January', 'February', 'March',
            'April', 'May', 'June',
            'July', 'August', 'September',
            'October', 'November', 'December'
        ],
        'ru': [
            'Январь', 'Февраль', 'Март',
            'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь',
            'Октябрь', 'Ноябрь', 'Декабрь'
        ]
    }
    return MONTH[language][number - 1]

# E

def split_numbers(line):
    return tuple(map(int, line.split()))
    
    
