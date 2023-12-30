"""
单态模式的实现
"""
class Borg:
    # 类属性
    __shared_state = {'name': None}
    def __init__(self):
        self.__dict__ = self.__shared_state


# 使用__new__方法实现单态模式
class NewBorg:
    __shared_state = {}
    # TODO 1 重新new方法
    def __new__(cls, *args, **kwargs):
        # TODO 2 生成shili
        borg_obj = super().__new__(cls, *args, **kwargs)
        # TODO 3 将实例的__dict__指向类属性__shared_state
        borg_obj.__dict__ = cls.__shared_state
        return borg_obj

    def __init__(self):
        self.name = 'Borg1'



if __name__ == '__main__':
    a = Borg()
    b = Borg()
    # 此时，如果对a设置属性age，则b也会被赋予属性age
    a.age = 20

    print(a.age)
    print(b.age)


    new_borg = NewBorg()
    new_borg_2 = NewBorg()
    print(f"更新name属性前：{new_borg.name}")
    # 更改name属性
    new_borg_2.name = "Borg2"
    print(f"更新name属性后：{new_borg.name}")