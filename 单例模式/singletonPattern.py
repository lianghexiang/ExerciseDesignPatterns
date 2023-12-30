# 经典单例模式
class Singleton(object):
    """
    经典单例模式：
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            _instance = super(Singleton, cls).__new__(cls)
            cls._instance = _instance
        return cls._instance

    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return self.name



class LazySingleton:
    """
    懒汉模式：
    """
    __instance = None
    def __init__(self):
        if not LazySingleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance


# TODO 2 装饰器单例模式
def singleton_decorator(cls):
    # 创建一个存储类实例的字段
    _instances = {}
    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return wrapper

@singleton_decorator
class DecoratorSingleton:
    def __init__(self, name=None):
        self.name = name


if __name__ == '__main__':

    st = Singleton("Tom")
    st2 = Singleton("Jerry")
    print(st)
    print(st2)

    dt_singleton = DecoratorSingleton("Decorator Singleton")
    print(dt_singleton)
    dt_singleton2 = DecoratorSingleton("Decorator Singleton2")
    print(dt_singleton2)

