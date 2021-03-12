'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
'''


def is_digit_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def is_digit_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def my_func(x, y):
    return x ** y

def my_func_v2(x, y):
    n = 1
    st = 1
    while n <= abs(y):
        st = st * x
        n = n + 1
    return 1 / st


while 1 == 1:
    x = input('Введите действительное положительное число: ')
    y = input('Введите целое отрицательное число: ')

    if is_digit_float(x):
        if is_digit_int(y):
            if float(x) > 0 and int(y) < 0:
                print(my_func(float(x), int(y)))
                print(my_func_v2(float(x), int(y)))
                break
            else:
                print('Повторите ввод, х>0, y<0')
        else:
            print('У не целое число, повторите ввод')
    else:
        print('X не число, повторите ввод')
