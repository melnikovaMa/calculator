a = 'да'
print('Привет')
print('Эта программа может выполнять:')
print("сложение - '+'")
def s(x, y):
    print(x, '+', y, '=', x + y)

print("вычитание - '-'")
def v(x, y):
    print(x, '-', y, '=', x - y)

print("умножение - '*'")
def u(x, y):
    print(x, '*', y, '=', x * y)

print("деление - '/'")
def d(x, y):
    print(x, '/', y, '=', x / y)

print("целочисленное деление - '//'")
def c(x, y):
    print(x, '//', y, '=', x // y)

print("взятие остатка - '%'")
def o(x, y):
    print(x, '%', y, '=', x % y)

print("возведение в степень - '**'")
def vs(x, y):
    print(x, '**', y, '=', x ** y)

print("квадратный корень числа - '///'")
def k(x):
    print(x, '/// =', x ** 0.5)

print("переводить из любой системы счисления в десятичную - '<>'")
def p(x, y):
    print(x, '=', int(str(x), y))

print("анализ числа - '^'")
def ch(x):
    # 1 пункт про разряды
    b = len(x)
    if str(b)[-1] == '1':
        print('1)', b, 'разряд')
    elif str(b)[-1] == '2' or str(b)[-1] == '4' or str(b)[-1] == '3':
        print('1)', b, 'разряда')
    else:
        print('1)', b, 'разрядов')
    # 2 пункт про количество цифр
    d = dict()
    for i in str(x):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print('2)', end='')
    for i in d:
        print(i, '=', d[i], 'р.')
    # 3 пункт про четность
    if x % 2 == 0:
        print('3) четное')
    else:
        print('3) не четное')
    # 4 пункт про сумму цифр
    c = 0
    for i in str(x):
        c += int(i)
    print('4) сумма цифр =', c)
    # 5 пункт про простое число
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
        print('5) простое число')
    else:
        print('5) непростое число')
        p = ''
        for i in range(1, x + 1):
            if x % i == 0:
                p = p + ', ' + str(i)
        print('делители:', p)
    # пункт 6 про полный квадрат
    if round(x ** 0.5) ** 2 == x:
        print('6) является полным квадратом числа', x ** 0.5)
    else:
        print('6) не является полным квадратом')
    s = ['', 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    r = ''
    if len(str(x)) > 3 and len(str(x)) < 7:
        for i in s:
            if int(str(x)[:-3]) < i:
                r = r + str(index(i) - 1)
        for i in s:
            if str(x)[-1] == str(i)[-1]:
                r = r + str(index(i) - 1)
    if len(str(x)) <= 3:
        for i in s:
            if int(str(x)) < i:
                r = r + str(index(i) - 1)
    if r ** 3 == x:
        print('7) является полным кубом числа', r)
    else:
        print('7) не является полным кубом')


while a == 'да' or a == 'lf':
    print('Напиши что ты хочешь от компуктера')
    print('Напиши певрое число')
    x = input()
    print('Напиши действие')
    c = input()
    print('Напиши второе число')
    if c == '///' or c == '^':
        print("Если второе число не требуется нажмите Enter")
    if c == '<>':
        print('Ecли требуется перевод в десятичную систему счисления введите число системы счисления первого числа')
    y = input()
    if x.isdigit():
        x = int(x)
    if y.isdigit():
        y = int(y)
    if c == '+':
        s(x, y)
    elif c == '-':
        v(x, y)
    elif c == '*':
        u(x, y)
    elif c == '/':
        d(x, Y)
    elif c == '//':
        c(x, y)
    elif c == '%':
        o(x, y)
    elif c == '**':
        vs(x, y)
    elif c == '///':
        k(x)
    elif c == '<>':
        p(x, y)
    elif c == '^':
        ch(x)
    else:
        print('Ошибка')
    if str(type(x)) != "<class 'int'>" and (str(type(y)) != "<class 'int'>" or y != ''):
        print('Ошибка')
    print('Желаете ли вы выполнить еще действие?')
    a = input()
print('Пока')
