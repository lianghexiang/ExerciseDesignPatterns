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

if __name__ == '__main__':

    st = Singleton("Tom")
    print(st)
    print(st.name)
    st2 = Singleton("Jerry")
    print(st2)
    print(st2.name)
    quit()

    s = LazySingleton()  # class initialized, but object not created
    # print("Object created", Singleton.getInstance())  # Object gets created

    s1 = LazySingleton()  # instance already created
    s.getInstance()
    s2 = LazySingleton()
    s3 = LazySingleton()
    print(s2.getInstance())
