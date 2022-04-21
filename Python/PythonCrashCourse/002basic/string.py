####

# * title upper lower
# ^modify upper case
name = 'py PY pY'
print(name.title())  # Py Py PY
print(name.upper())  # PY PY PY
print(name.lower())  # py py py


# * strip rstrip lstrip
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
