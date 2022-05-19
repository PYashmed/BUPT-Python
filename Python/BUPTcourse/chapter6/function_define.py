# def change(a):
#     a = 10
#     print("a in function:", a)
#     return a


# a = 0
# print("a out func:", a)
# result = change(a)
# print("a after func:", a)
# print("result of func:", result)


# def f(x):
#     x[0] = 999
#     print("after func:", x)
#     return x


# a = [1, 2, 3, 4, 5]
# print("a before", a)
# f(a)
# b = [0, 1]
# b = f(b)
# print("b after:", b)

# def no_return():
#     print("no return, equals return None")


# def just_return():
#     print("just return, equals return None")


# def return_variable():
#     print("return a object")
#     return 999


# def return_variables():
#     print("return objects")
#     return 999, 888, 777


# no_return()
# just_return()
# a = return_variable()
# print("a =", a)
# b, c, d = return_variables()
# print("b c d=", b, c, d, type(return_variables()))


# num = 10
# print("num is:", num)


# def change_global_num():
#     global num
#     num = 100
#     print("num in func is:", num)


# change_global_num()
# print("num after func:", num)


# def print_type(x):
#     print("parameter type:", type(x))


# print_type(1)
# print_type(1.1)
# print_type([1, 2])
# print_type((1, 2))
# print_type({1, 2})
# print_type({"key1": 1, "key2": 2})

# def print_type(x):
#     print(type(x))


# def traverse_seq(a):
#     for i in a:
#         print_type(i)


# traverse_seq([1, [1, 2], (1, 2), {1, 2}, {"key1": 1, "key2": 2}])


# def f(x):
#     return "value"+str(x)


# list0 = [1, 2, 3, 4]
# new_dict = {f(x): x for x in list0}
# print(new_dict)

# def func(a, b=2, c=3, d=4):
#     print("a b c d=", a, b, c, d)


# func(4)

# def hybrid_func(a, b, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10):
#     print("list:", a, b, c, d, e, f, g, h, i, j)


# hybrid_func(1, 2, a=3)


# def variable_func(*a, **k):
#     print(a, k)


# a1 = (1, 2, 3)
# k1 = {"key1": 1, "key2": 2, "key3": 3}
# variable_func(*a1, **k1)


# def hybrid_func(a, b=1, *c, **d):
#     print("formal:", a, b, "variable tuple:", c, "named variable:", d)


# hybrid_func(1, 3, 'a', [2, 3], {"key1": 1, "key2": 2}, x=3, h=7)

# def f(a, b=1, c=2, *d, **e):
#     print(a, b, c, d, e)


# t1 = (1, 2, 3, 4, 5)
# k1 = {"key1": 1, "key2": 2, "key3": 3}
# f(*t1, 9, 8, 7, **k1, x=2)

# def f(a, b=1, c=2, *d):
#     print(a, b, c, d)


# f(1, (4, 5, 6), c=99)
