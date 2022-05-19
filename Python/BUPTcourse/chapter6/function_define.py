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

def func(a, b=2, c=3, d=4):
    print("a b c d=", a, b, c, d)


func(4)

