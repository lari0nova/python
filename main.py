#OP задание 3

#Медицинская анкета

name=input('Укажите Ваше имя: ')
surname=input('Укажите Вашу фамилию')

age=int(input('Укажите Ваш возраст'))

weight=int(input('Укажите массу вашего тела'))
print(''
      '')
if age < 30 and weight > 50 and weight < 120:
    print('Вы в хорошем состоянии')
if age > 30 or weight <50 and weight > 120:
    print('Вам требуется заняться собой')




