# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#  Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding="utf-8") as my_file:
    content = my_file.read()
    content = content.split('\n')
    my_list = []
    my_list_1 = []
    for i in content:
        i = i.split(' ')
        if float(i[1]) < 20000.0:
            my_list.append(i[0])
        my_list_1.append(float(i[1]))

    print('Список сотрудников с окладом менее 20000:{}'.format(my_list))
    print('Средняя величина дохода сотрудника:{}'.format(sum(my_list_1)/len(my_list_1)+1))


