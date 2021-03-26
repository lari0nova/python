my_list=[123, 'first_list', 23.2, False]
print(my_list)

print(type(my_list))
print('4-ый элемент списка: {}'.format(type(my_list[-1])))
print('3-ий элемент списка: {}'.format(type(my_list[-2])))
print('2-ой элемент списка: {}'.format(type(my_list[1])))
print('1-ый элемент списка: {}'.format(type(my_list[0])))


n=1
for element in my_list:
    print('{} элемент списка: {}'.format(n, type(element)))
    n=n+1






