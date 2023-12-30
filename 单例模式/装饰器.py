# 装饰器
def decorator(func):
    """
    :param func: 被装饰函数
    :return: 返回内层函数
    """
    def wrapper(*args, **kwargs):# *args和**kwargs主要是被装饰函数所需的参数
        # 函数执行前的操作
        print("Start:")
        func(*args, **kwargs)
        # 函数执行后的操作
        print("End")
    return wrapper


# 基本函数
# def test(text):
#     print(text)


# 使用装饰器后的函数
@decorator
def test(text):
    print(text)


if __name__ == '__main__':
    test('装饰器')