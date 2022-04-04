from lib1 import module1 as m1
def f():
    print("我是来自module2的f()函数")
    m1.f()