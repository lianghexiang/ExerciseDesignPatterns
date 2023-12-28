# 经典单例模式
class ExerciseSinglePattern:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance

        