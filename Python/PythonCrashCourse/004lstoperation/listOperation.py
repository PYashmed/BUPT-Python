#
from numpy import square


a = ["py", 0, 1, 2, 3, "hello", "world"]

# * Traverse a list
# ^ circulation-----for
for i in a:
    print(i)  # py 0 1 2 3 hello world

# * create a list of value
# ^ range : evenly spaces value form a list,
# ^ range(a,b,c) from a to b with step c, but b will not in the list
for i in range(1, 6):
    print(i)  # 1 2 3 4 5
b = list(range(2, 7))
print(b)  # [2, 3, 4, 5, 6]
c = list(range(1, 10, 3))
print(c)  # [1, 4, 7]
# ^ example : squares
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# equals to
squares1 = [i**2 for i in range(1, 11)]
print(squares1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# * find the minimum / maximum / sum
# ^ min(list),max(list),sum(list)
# ! all are function
print(max(squares))  # 100
print(min(squares))  # 1
print(sum(squares))  # 385

# * list slice
# ^ [a:b]from a to b without b
print(b[0:2])  # [2, 3]
print(b[-3:])  # [4, 5, 6] #^ from antepenultimate to the end
print(b[:-3])  # [2, 3] #^ from the first to the third to last

# * Traverse section
for i in b[0:3]:
    print(i)  # 2 3 4

# * copy list
bcp = b[:]
print(bcp)  # [2, 3, 4, 5, 6]

# * tuple
# ^ the only different between list and tuple is tuple can't be modified
# ^ (  ,  )
A = ("py", 0, 2, 3)
print(A)  # ('py', 0, 2, 3)
print(A[1: 3])  # (0, 2)

