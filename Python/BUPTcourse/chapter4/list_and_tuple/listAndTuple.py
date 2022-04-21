# -*-coding=utf-8-*-
# ! basic different
# * list
# ^ [item1,item2,item3]
# ^ list can be modified
a = [1, 2, 'a', "hello"]

# * tuple
# ^ (item1,item2,item3)
# ^ tuple can't be modified
# ^ one item tuple : (item1,)
b = (1, 2, 3)
c = (1,)
print(type(c), type((1)))  # <class 'tuple'> <class 'int'>

# * convert : tuple() list()
# ^ in fact ,tuple(),list() is construct function
print(tuple(a))  # (1, 2, 'a', 'hello')
print(list(b))  # [1, 2, 3]


# ! same operate
# * index
a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)
print(a[0], b[0])  # 2 2
print(a[-1], b[-1])  # 5 5
# ^ index mustn't cross the border
# print(a[7]) IndexError: list index out of range

# * partition
print(a[1:3], b[1:3])  # [2, 3] (2, 3)
print(a[-5:-1], b[-5:-1])  # [1, 2, 3, 4] (1, 2, 3, 4)
print(a[-4:], b[-4:])  # [2, 3, 4, 5] (2, 3, 4, 5)
# ^ partition can cross the border
print(a[-6:], b[-8:])  # [1, 2, 3, 4, 5] (1, 2, 3, 4, 5)
# ^ -x : +y
print(a[-6:2])  # [1, 2]
# a[-6:2] == intersection of a[-6:0] and a[0:2]

# * merge : +
# ^ same class can be merged by + ,this operate will create a new object in memory
a1 = [1, 2, 3]
a2 = [4, 5]
b1 = (1, 2, 3)
b2 = (4, 5)
print(a1+a2, a1, a2)  # [1, 2, 3, 4, 5] [1, 2, 3] [4, 5]
print(b1+b2, b1, b2)  # (1, 2, 3, 4, 5) (1, 2, 3) (4, 5)

# * repeat : *
# ^ will create a new object
print(a*2, a)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
# ^ create a none tuple with 10 space
print((None,)*10)  # (None, None, None, None, None, None, None, None, None, None)

# * in  /  not in
a = [1, 2, 3]
print(1 in a, 4 not in a)  # True True

# * len() max() min()
# ^ number < lower case < upper case < Chinese
t = ['A', '1', 'a', '你']
print(len(t), max(t), min(t), sorted(t))  # 4 你 1 ['1', 'A', 'a', '你']

# * derived
# ^ list derived
a = [1, 2, 3, 4, 5]
# want to get [1,9,25]
list2 = []
for x in a:
    if x % 2 != 0:
        list2.append(x**2)
print(list2)  # [1, 9, 25]
# so complex
list3 = [x**2 for x in a if x % 2 != 0]
print(list3)  # [1, 9, 25]
# ^ tuple derived
tuple3 = tuple([x**2 for x in a if x % 2 != 0])
print(tuple3)  # (1, 9, 25)

# * generator ()
# ^ this action doesn't need whole memory
g = (x*2 for x in [1, 2, 3, 4, 5, 6, 7, 8])
print(type(g))  # <class 'generator'>
# a 8-space memory isn't required
# ^ next() make generator build next object
print(next(g))  # 2
print(next(g))  # 4
for x in g:
    if x > 10:
        print(x)  # 12
        break
    print(x, end=" ")  # 6 8 10
    # 6 8 10 12
# ^ when use generator ,it likes there is an index so next is 14
print(next(g))  # 14

# * generator function : yield
# ^ we use generator to reduce the memory use,especially when some functions are very complex


def func0(x):
    '''in fact this function may be very complex'''
    return x*3


list1 = [1, 2, 3, 4, 5]


def g_func1(list1):
    for i in list1:
        if i % 2 != 0:
            yield func0(i)


g = g_func1(list1)
# <generator object g_func1 at 0x0000013EBA463890> <class 'generator'>
print(g, type(g))
for i in g:
    print(i, end=" ")  # 3 9 15
