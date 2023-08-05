'''Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.'''
from klass_work.task_6 import Animals
from klass_work.task_5 import Fish, Birds, Insects

class Factory(object):

    def __init__(self, animal:type , *args):
        if animal == Fish:
            self.anim = Fish(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
        elif animal == Birds:
            self.anim = Birds(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
        elif animal == Insects:
            self.anim = Insects(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
        else:
            self.animal = 'какашка'


f = Factory(Fish, *('Карась', 'Плавник', ['золотой', 'серовато-желтый'], 'чашуя', 10, (0, 50), ['Река', 'Озеро']))
f.anim.information()
