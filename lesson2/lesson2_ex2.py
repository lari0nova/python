l = input('Введите элементы через пробел :')

list_my = l.split(' ')
print(list_my)

j=0
for i in range(int(len(list_my)/2)):
    list_my[j], list_my[j+1] = list_my[j+1], list_my[j]
    j=j+2

print(list_my)


for i in range(0, len(list_my)//2*2, 2):
    list_my[i], list_my[i+1] = list_my[i+1], list_my[i]


print(list_my)






