# TODO 1 经典单例模式
class ExerciseSinglePattern:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, a, b):
        print('__init__')
        self.a = a
        self.b = b


if __name__ == '__main__':
    sp = ExerciseSinglePattern('a', 'b')
    sp2 = ExerciseSinglePattern('c', 'd')

    print(sp)
    print(sp2)
    print(sp.a)
    print(sp2.a)
