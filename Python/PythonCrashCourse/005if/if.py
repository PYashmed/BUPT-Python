#
# * condition test
# ^ == != < <= > >= return bool
print(3 == 4)  # False
print('a' != 'b')  # True

# * use and / or to compare more than one at the same time
print(3 != 4 and 'a' != 'b')  # True

# * in : check if a is in list
# * not in : check not in
a = [1, 2, 3, 4, 5, 6, 'py']
print('PY' not in a)  # True
print(1 in a)  # True

# *---------if-----------
age = 10
if age > 18:
    age -= 1
    print(age)  # if--false
else:
    age += 1
    print(age)  # 11

# * elif equals to else if