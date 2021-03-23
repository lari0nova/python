# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('text_5.txt', 'w', encoding="utf-8") as file_number:
    number = input('Введите числа, разделенные пробелом: \n')
    file_number.writelines(number)

with open('text_5.txt', 'r', encoding="utf-8") as file_number:
    number_1 = file_number.read()
    my_list = number_1.split(' ')
    print(sum(map(int, my_list)))
