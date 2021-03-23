# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return '{} {} поехала!'.format(self.color,self.name)

    def stop(self):
        return '{} остановилась!'.format(self.name)

    def turn(self, direction):
        return '{} повернула {}!'.format(self.name, direction)

    def show_speed(self):
        return 'Скорость на данный момент: {}!'.format(self.speed)


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if int(self.speed) > 60:
            return 'Вы превысили максимальнодопустимую скорость! Ваша скорость {}'.format(self.speed)
        else:
            return 'Ваша скорость не превышает разрешенную максимальную'


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            return 'Вы превысили максимальнодопустимую скорость! Ваша скорость {}'.format(self.speed)
        else:
            return 'Ваша скорость не превышает разрешенную максимальную'


town = TownCar('Toyta camry', 'Белая', 90, False)
print('1. ' + town.go()+'\n'+ town.show_speed()+'\n'+ town.turn('направо')+'\n'+ town.turn('налево')+'\n'+ town.stop())

work = WorkCar('КАМАЗ', 'Оранжевый', 30, False)
print('2. ' + work.go()+'\n'+ work.show_speed()+'\n'+ work.turn('налево')+'\n'+ work.turn('направо')+'\n'+ work.stop())

policecar = PoliceCar('Skoda octavia', 'Бело-синяя', 75, True)
print('3. ' + policecar.go()+'\n'+ policecar.show_speed()+'\n'+ policecar.turn('налево')+'\n'+ policecar.turn('направо')+'\n'+ policecar.stop())

sportcar = SportCar('Porsche Panamera', 'Красная', 140, False)
print('4. ' + sportcar.go()+'\n'+ sportcar.show_speed()+'\n'+ sportcar.turn('налево')+'\n'+ sportcar.turn('направо')+
      '\n'+ sportcar.stop())