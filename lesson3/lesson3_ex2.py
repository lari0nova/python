'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def personal_inf(name, surname, year, city, email, tel_number):
    print(f"name-{name}; surname-{surname}; year-{year}; city-{city}; email-{email}; tel_number-{tel_number}")


name = (input('Укажите Ваше имя: '))
surname = (input('Укажите Вашу фамилию: '))
year = (input('Укажите год Вашего рождения: '))
city = (input('Укажите город проживания: '))
email = (input('Укажите адрес электронной почты: '))
tel_number = (input('Укажите Ваш контактный номер телефона: '))

personal_inf(name, surname, year, city, email, tel_number)
