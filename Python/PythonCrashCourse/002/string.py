####
# ^string is what enclosed in "" or ''
# ^in python ,we make no distinction between "" and ''
# ^so string is flexible
print("hello")
print('world')
print("PY says 'hello' world")
print('hello "world"')

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
print(d)
print(a.title()+" "+b+" "+c.title())
