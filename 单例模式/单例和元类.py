a = 10
print(type(a))  # <class 'int'>


print(type(int))  # <class 'type'>


# 简单的元类示例
class MyInt(type):
    # __call__方法在类以函数方式调用的时候被触发
    def __call__(cls, *args, **kwargs):
        print("*** 自定义元类 Int类型 ***", args)
        print("在这里可以自定义你自己的类的行为.....")
        return type.__call__(cls, *args, **kwargs)

# 使用上面自定义的元类来创建int类型
class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 使用元类创建单例
class MetaSingleton(type):
    _instances = {}
    # 覆盖type的__call__方法

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    def __init__(self, level):
        self.level = level


if __name__ == '__main__':
    my_int = int(10, 20)

    logger_1 = Logger('info')
    logger_2 = Logger('error')
    print(logger_1)
    print(logger_2)
    print(logger_1.level)
    print(logger_2.level)

