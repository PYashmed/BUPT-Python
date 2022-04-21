#
# ^string is what enclosed in "" or '' also ''' '''
# ^in python ,we make no distinction between "" and ''
# ^but we can't use "/"" in "" or '/'' in ''
# ^so string is flexible


# * ''  ""  ''''''  """"""
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


# * ESC escape character : \
# ^ \ (when in the end) line continuation
print("2222\
2222")  # 22222222
# ^ remove esc
print(r"\n\t\\\a")  # \n\t\\\a


# * string + string
# ^merge string
a = 'py'
b = 'love'
c = 'lmc'
d = a+" "+b+" "+c
print(d)  # py love lmc
print(a.title()+" "+b+" "+c.title())  # Py love Lmc


# * coding : utf-8
# ^ simplify Chinese
list1 = ['a', 'b', 'f', '你', '好耶']
for i in list1:
    if '\u4E00' < i < '\u9FEF':
        print(i)
#你
#好耶

