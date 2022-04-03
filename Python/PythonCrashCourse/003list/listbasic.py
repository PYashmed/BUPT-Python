#
# ^ different from cpp, in python a list could contain every elements, different types is valid
# ^ also be enclosed by []

from cv2 import sort


a = [0, "hello", "PY", 1.1, True, ("py", 2), [2, "p"]]

# ^ print a will output the list with []
print(a)  # [0, 'hello', 'PY', 1.1, True, ('py', 2), [2, 'p']]

# ^remember in Python, everything is object
print(a[1].title())  # Hello

# ^ the index , begin from 0
# ^ particularly, in python, we can use -1 as the index of the last element, no matter how long the list is
print(a[0])  # 0
print(a[-1])  # [2, 'p']
print(a[-2])  # ('py', 2)

# & some operators of list(object)
# * append : add a element behind the end
# ^ x.append(object)
a.append("world")
print(a[-1])  # world

# * insert : add a element at any position you want
# ^ x.insert((int)location,object)   this location means in the new list ,the new element's location
a.insert(0, "Python")
print(a)  # ['Python', 0, 'hello', 'PY', 1.1, True, ('py', 2), [2, 'p'], 'world']

# * del : delete the element
# ! del is a statement, not a operator of object
del a[2]
print(a)  # ['Python', 0, 'PY', 1.1, True, ('py', 2), [2, 'p'], 'world']

# * pop : delete the last one and delete it in the list
# ^ pop((int)location) when no actual parameter, it will pop the last one
print(a.pop(2))  # PY
print(a)  # ['Python', 0, 1.1, True, ('py', 2), [2, 'p'], 'world']

# * remove : delete by value
# ^ remove(object)  if there is two same object,it'll just delete the first one
a.remove([2, 'p'])
print(a)  # ['Python', 0, 1.1, True, ('py', 2), 'world']

# * sort : sort the list by ASCII permanently
# ! but sort use "< >" and it can't compare str with int
b = ['a', 'b', 'A', 'B']
b.sort()
print(b)  # ['A', 'B', 'a', 'b']
# ^ sort have parameter reverse
b.sort(reverse=True)
print(b)  # ['b', 'a', 'B', 'A']

# * sorted : sort the list by ASCII temporarily
# ! sorted is a function ,not a operator of object
c = [4, 2, 3, 1]
print(sorted(c))  # [1, 2, 3, 4]
print(c)  # [4, 2, 3, 1]

# * reverse : reverse the list
print(a)  # ['Python', 0, 1.1, True, ('py', 2), 'world']
a.reverse()
print(a)  # ['world', ('py', 2), True, 1.1, 0, 'Python']

# * len : return the length of the list
# ! len is a function
print(len(a))  # 6
