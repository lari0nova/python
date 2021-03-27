# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Всего затрачено ткани = {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'test1'


class Coat(Clothes):
    def consumption(self):
        return [f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} м. ткани', (self.param / 6.5 + 0.5)]

    def abstract(self):
        pass


class Costume(Clothes):
    def consumption(self):
        return [f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} м. ткани', 2 * self.param + 0.3]

    def abstract(self):
        pass


coat = Coat(900)
costume = Costume(35)

print(coat.consumption()[0])
print(costume.consumption()[0])
print('Общий расход: {:.2f}'.format(coat.consumption()[1] + costume.consumption()[1]))
