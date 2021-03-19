# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('first.txt', 'r', encoding="utf-8") as my_file:
    content = my_file.readlines()
    print(content)
    print('Количество строк в файле: {}'.format(len(content)))

    i = 1
    for el in content:
        print('Количество слов в {}-й строке: {}'.format(i, len(el.split(' '))))
        i += 1
