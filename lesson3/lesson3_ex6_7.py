'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(word):
    a_lit = ord(word[0])
    a_big = chr(a_lit - 32)
    return a_big + word[1:]


word = input('Введите слово из маленьких латинских букв: ')

i = 0
while i < len(word):
    if ord(word[i]) >= 97 and ord(word[i]) <= 122:
        i = i + 1
    else:
        print(('Ошибка!Необходимо ввести слово, состоящее из маленьких латинских букв!'))
        break
    if i == len(word) - 1:
        print(int_func(word))


def str_func(str):
    list = str.split(' ')
    list_new = []

    for n in list:
        i = 0
        while i < len(n):
            if ord(n[i]) >= 97 and ord(n[i]) <= 122:
                i = i + 1
            else:
                print('Ошибка!Необходимо ввести слова, состоящие из маленьких латинских букв!')
                break
        if i == len(n):
            list_new.append(int_func(n))

    return " ".join(list_new)


str_my = input('Введите несколько слов, разделенных пробелом: ')

print(str_func(str_my))
