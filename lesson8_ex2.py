# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class MyException(Exception):

    def __init__(self, txt):
        self.txt = txt


divider = int(input('Введите делимое: '))
denominator = int(input('Введите делитель: '))

try:
    res = round(divider / denominator, 2)
except ZeroDivisionError as err:
    print("Число нельзя делить на 0!")
else:
    print(res)
finally:
    print('The end')
