from abc import ABCMeta, abstractmethod
"""
简单工厂模式 ：允许接口创建对象，但不会暴露对象的创建逻辑。
工厂方法模式 ：允许接口创建对象，但使用哪个类来创建对象，则是交由子类决定的。
抽象工厂模式 ：抽象工厂是一个能够创建一系列相关的对象而无需指定/公开其具体类的接口。该模式能够提供其他工厂的对象，在其内部创建其他对象。
"""

# 简单工厂模式
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass


class Dog(Animal):
    def say(self):
        print("汪汪汪...")


class Cat(Animal):
    def say(self):
        print("喵喵喵...")


# 创建工厂
class AnimalFactory:
    def make_sound(self, animal_type):
        # 实例化具体的Animal
        animal = eval(animal_type)()
        animal.say()


# 客户端代码
if __name__ == '__main__':
    # 客户端只需要通过工厂来生成animal即可
    aml_fty = AnimalFactory()
    aml_fty.make_sound("Cat")
    aml_fty.make_sound("Dog")

