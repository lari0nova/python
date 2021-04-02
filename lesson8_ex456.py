# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

import datetime
import pprint

class Sklad:
    def __init__(self):
        self._dict = {}
        self._dict_move = {}

    def add_to(self, equipment):
        nm = equipment.group_name()
        if not(nm in self._dict):
            self._dict.setdefault(equipment.group_name(),
                                  {equipment.sn: [equipment.name, equipment.make, equipment.year]})
        else:
           a = self._dict[equipment.group_name()]
           a.update({equipment.sn: [equipment.name, equipment.make, equipment.year]})
           self._dict[nm]= a
    def extract(self, name, sn, new_dep):
        if self._dict[name]:
           if sn in self._dict[name]:
               del self._dict[name][sn]
               self._dict_move[sn] = [new_dep, str(datetime.datetime.now())]
           else: print('S/N not found')


class Equipment:
   def __init__(self, sn, name, make, year):
    self.sn = sn
    self.name = name
    self.make = make
    self.year = year
    self.group = self.__class__.__name__

   def group_name(self):
       return f'{self.group}'

   def __repr__(self):
       return f'{self.sn} {self.name} {self.make} {self.year}'

class Printer(Equipment):
    def __init__(self, series, sn, name, make, year):
       super().__init__(sn, name, make, year)
       self.series = series

    def __repr__(self):
        return f'{self.sn} {self.name} {self.series} {self.make} {self.year}'

    def action(self):
        return 'Печатает'

class Scaner(Equipment):
    def __init__(self, sn, name, make, year):
        super().__init__(sn, name, make, year)

    def action(self):
        return 'Сканирует'

class Xerox(Equipment):
    def __init__(self, sn, name, make, year):
        super().__init__(sn, name, make, year)

    def action(self):
        return 'Копирует'

sklad = Sklad()
# создаем объект и добавляем
scaner = Scaner('512-612-712', 'hp', '321', 90)
sklad.add_to(scaner)
scaner = Scaner('423-123-712', 'hp', '311', 97)
sklad.add_to(scaner)
scaner = Scaner('512-111-712', 'hp', '330', 99)
sklad.add_to(scaner)
printer = Printer('e-320', '111-612-712', 'sony', 126, 2018)
sklad.add_to(printer)
xerox = Xerox('631-411-777', 'M350', 'ABC', 2021)
sklad.add_to(xerox)

# выводим склад
print('Склад после наполнения')
pprint.pprint(sklad._dict, width=10)
# забираем со склада, и указываем подразделение, куда передали
sklad.extract('Scaner','423-123-712','fin_dep')
# забираем со склада оборудование, которого там нет, выводим сообщение об ошибке.
sklad.extract('Scaner','423-000-712','fin_dep')
print()
print()
print('Склад после перемещения элемента')
pprint.pprint(sklad._dict)
print()
print()
print('Запись перемещений')
print(sklad._dict_move)
