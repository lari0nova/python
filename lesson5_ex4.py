# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file_new = []
with open('text_4.txt', 'r', encoding="utf-8") as my_file:
    content = my_file.read().split('\n')
    for el in content:
        el = el.split(' ')
        if el[0] in el:
            file_new.append(my_dict.get(el[0]) + ' - ' + el[2] + '\n')


with open('new_text_4.txt', 'w', encoding="utf-8") as my_file2:
    my_file2.writelines(file_new)



