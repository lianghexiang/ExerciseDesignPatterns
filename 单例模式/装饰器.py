# 装饰器
import time
import functools


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


# 带有参数的装饰器
def logger_decorator(log_info1, log_info2):
    # 装饰器
    def decorator(func):
        # 内层函数
        def wrapper(*args, **kwargs):
            print(f"{func.__name__}:{log_info1} Time:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
            func(*args, **kwargs)
            print(f"{func.__name__}: {log_info2} Time:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        return wrapper
    return decorator

# 带有参数的装饰器使用方法如下
@logger_decorator("Start...", "...End")
def test2():
    print("正在插入数据")
    time.sleep(5)

# functools.wraps来替换函数的签名
def wraps_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Do Something......")
        return func(*args, **kwargs)
    return wrapper

@wraps_decorator
def wraps_test(text):
    print(text)
    time.sleep(2)

if __name__ == '__main__':
    # test('装饰器')
    # id_test2 = test2
    # print(test2)

    # 我们如果不使用functools.wraps
    func_name = wraps_test.__name__
    print(f"wraps_test函数名称：{func_name}")