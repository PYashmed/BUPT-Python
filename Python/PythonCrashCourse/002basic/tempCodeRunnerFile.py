####
# ^string is what enclosed in "" or '' also ''' '''
# ^in python ,we make no distinction between "" and ''
# ^but we can't use "/"" in "" or '/'' in ''
# ^so string is flexible
from __future__ import print_function


print("hello")
print('world')
print("PY says 'hello' world")
print('hello "world"')
# ^ strings in ''' ''' or """ """ will keep its format
a = '''hello 
            world'''
print(a)
# hello
#             world

# * ESC escape character
# ^ \ (when in the end) line continuation
print("2222\
2222")  # 22222222

# ^ \n line break
print("111\n222")

# ^modify upper case
name = 'py PY pY'
print(name.title())  # Py Py PY
print(name.upper())  # PY PY PY
print(name.lower())  # py py py

# ^merge string
a = 'py'
b = 'love'
c = 'lmc'
d = a+" "+b+" "+c
print(d)  # py love lmc
print(a.title()+" "+b+" "+c.title())  # Py love Lmc

# ^Python can strip lead and trail space
a = 'PY       '
b = '       PY'
# ^rstrip---right strip,strip the spaces at the end
print(a.rstrip())  # PY
# ^lstrip---left strip ,strip the space in the front
print(b.lstrip())  # PY

# ^but this function just remove the spaces temporary
b.lstrip()
print(b)  # 'PY     '

# ^to permanently remove the space ,it needs to be assigned to a variable
c = b.lstrip()
print(c)  # PY
b = b.lstrip()
print(b)  # PY

# ^strip can remove the space both before and after
c = '    PY    '
print(c.strip()+'0')  # PY0
