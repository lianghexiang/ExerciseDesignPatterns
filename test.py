import unittest


class MyTestCase:
    def __init__(self, name):
        self.name = name



if __name__ == '__main__':
    m = MyTestCase("a")
    print(m.name)
