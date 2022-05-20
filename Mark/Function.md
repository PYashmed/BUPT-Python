# Function

---

## 6.1function define

### 6.1.2 Build_in function

[Python3.9---Build_in_function](https://docs.python.org/zh-cn/3.9/library/functions.html)

| name  | index |
| ----- | ----- |
| abs() |

### 6.1.3 self_define function

#### Define Grammar

```python
{
    def functionName(arg1,arg2):
        ''' function describe'''
        print(arg1+"hello"+arg2)
        return arg1+arg2
}
```

### 6.1.4 transfer parameters

#### (1) By value

***Immutable objects*** transfer value by formal parameter, change the value of formal parameter won't change the passed variable *( because the object can't be changed )*

```python
{
def change(a):
    a = 10  
    print("a in function:", a)
    return a

a = 0
print("a out func:", a)
result = change(a)
print("a after func:", a)
print("result of func:", result)
}
```

>a out func: 0
a in function: 10
a after func: 0
result of func: 10

***a = 0 wasn't changed***

#### (2) By index

***Variable objects*** transfer value by index, if change the parameter in func,the value of variable will be changed

```python
{
def f(x):
    x[0] = 999
    print("after func:", x)
    return x


a = [1, 2, 3, 4, 5]
print("a before", a)
f(a)
b = [0, 1]
b = f(b)
print("b after:", b)
}
```

>a before [1, 2, 3, 4, 5]
after func: [999, 2, 3, 4, 5]
after func: [999, 1]
b after: [999, 1]

***a,b are changed***

### 6.1.5 function return value

each function can return **None / a variable / variables ( by tuple )**

```python
{
def no_return():
    print("no return, equals return None")


def just_return():
    print("just return, equals return None")


def return_variable():
    print("return a object")
    return 999


def return_variables():
    print("return objects")
    return 999, 888, 777


no_return()
just_return()
a = return_variable()
print("a =", a)
b, c, d = return_variables()
print("b c d=", b, c, d, type(return_variables()))
}
```

>no return, equals return None
just return, equals return None
return a object
a = 999
return objects
return objects
b c d= 999 888 777 **\<class 'tuple'>**

### 6.1.6 variable scope

#### (1) Local scope

Variable in function has **local scope**, just be valid in function

```python
{
num = 10
print("num is:", num)


def change_num():
    num = 100
    print("num in func is:", num)


change_num()
print("num after func:", num)
}
```

>num is: 10
num in func is: 100
num after func: 10

#### (2) Global scope

Variable out of function has **global scope**, if want to use global variable in function, **```global```** is needed

```python
{
num = 10
print("num is:", num)


def change_global_num():
    global num
    num = 100
    print("num in func is:", num)


change_global_num()
print("num after func:", num)
}
```

>num is: 10
num in func is: 100
num after func: 100

## 6.2 function call

### 6.2.1 call function

call function by use **```function_name(formal_parameter_list)```**
formal_parameter_list is an object of any type

```python
{
def print_type(x):
    print("parameter type:", type(x))


print_type(1)
print_type(1.1)
print_type([1, 2])
print_type((1, 2))
print_type({1, 2})
print_type({"key1": 1, "key2": 2})
}
```

>parameter type: **\<class 'int'>**
parameter type: **\<class 'float'>**
parameter type: **\<class 'list'>**
parameter type: **\<class 'tuple'>**
parameter type: **\<class 'set'>**
parameter type: **\<class 'dict'>**

### 6.2.2 call function in function

Just call function in function

```python
{
def print_type(x):
    print(type(x))


def traverse_seq(a):
    for i in a:
        print_type(i) # call function "print_type()"


traverse_seq([1, [1, 2], (1, 2), {1, 2}, {"key1": 1, "key2": 2}])
}
```

>\<class 'int'>
\<class 'list'>
\<class 'tuple'>
\<class 'set'>  
\<class 'dict'>

### 6.2.3 parameter passing

#### (1) Position pass ( default )

The formal parameter is matched with the variable list

```python
{
def func(a, b, c, d):
    print("a b c d=", a, b, c, d)


func(1, 2, 3, 4)
}
```

>a b c d= 1 2 3 4

#### (2) Name pass

The formal parameter is matched with the variable by name

```python
func(b=1, a=2, d=3, c=4)
```

>a b c d= 2 1 4 3

#### (3) Default pass ( default parameter )

If the formal parameter has default value, none pass is valid

```python
{
def func(a, b=2, c=3, d=4):
    print("a b c d=", a, b, c, d)


func(4)
}
```

>a b c d= 4 2 3 4

#### (4) Variable parameter (可变参数)

Function can receive more than formal parameter list

```python
def f(*c,**d)
```

**```*c```** will receive the variable beyond the formal parameter list, and pass it to the function by tuple
**```**d```** will receive the variable with name like **```x=10```**, and pass by dictionary

```python
{
def f(a, b, *c, **d):
    print("formal:", a, b, "variable tuple:", c, "named variable:", d)


f(1, 2, 3, 'a', [2, 3], {"key1": 1, "key2": 2}, x=3, h=7)
}
```

>formal: 1 2 variable tuple: (3, 'a', [2, 3], {'key1': 1, 'key2': 2}) named variable: {'x': 3, 'h': 7}

***named variable is not dictionary, dictionary is an object***

#### (5) Hybrid pass

Use position_pass, name_pass, Default pass and Variable parameter at the same time is valid

##### The priority

+ position_pass **>** name_pass **>** Default_pass **>** Variable parameter ( tuple ) **>** Variable parameter ( dictionary )
+ formal parameter list obeys the same rule
  
```python
{
def hybrid_func(a, b=1, *c, **d):
    print("formal:", a, b, "variable tuple:", c, "named variable:", d)


hybrid_func(1, 3, 'a', [2, 3], {"key1": 1, "key2": 2}, x=3, h=7)
}
```

>formal: 1 3 variable tuple: ('a', [2, 3], {'key1': 1, 'key2': 2}) named variable: {'x': 3, 'h': 7}

##### *Avoid repetition*

```python
hybrid_func(1, 2, a=3)
```

By position_pass a = 1, but a is given the value 3 by name_pass

>TypeError: hybrid_func() got multiple values for argument 'a'

**In fact, name_pass and variable ( tuple ) can't exist at the same time. Because name_pass should before variable parameter, but there mustn't be no_name_variable after name_pass, so nothing will pass to variable tuple.**

```python
{
def f(a, b=1,c=2,*d):
    print(a, b, c, d)
}
```

*Sometimes we cannot pass value to **```c```** if skip over **```b```** by name_pass and pass value to **```*d```** at the same time:*

**Want:**```1 1 99 (4,5,6)``` (variable list should skip over ```b```)

```python
f(1, c=99, (4, 5, 6))
```

>SyntaxError: positional argument follows keyword argument

```python
f(1, (4, 5, 6), c=99)
```

>1 (4, 5, 6) 99 () ------```b``` is changed

##### pass tuple to *x or dict to **y

Just use * or ** before tuple or dict as variable, tuple will pass like each variable, and dict will pass like each named variable

*~~But why not just use tuple and dict as objects~~*

```python
{
def f(a, b=1, c=2, *d, **e):
    print(a, b, c, d, e)


t1 = (1, 2, 3, 4, 5)
k1 = {"key1": 1, "key2": 2, "key3": 3}
f(*t1, 9, 8, 7, **k1, x=2)
}
```

>1 2 3 (4, 5, 9, 8, 7) {'key1': 1, 'key2': 2, 'key3': 3, 'x': 2}

### 6.2.4 Sequence derivation based on function

#### (1) list derivation

Generate a list by derivation

```python
{
def f(x):
    return "value"+str(x)


list0 = [1, 2, 3, 4]
new_list = [f(x) for x in list0]
print(new_list)
}
```

>['value1', 'value2', 'value3', 'value4']

#### (2) tuple derivation

Generate a tuple by derivation

```python
{
new_tuple = tuple(f(x) for x in list0)
print(new_tuple)
}
```

>('value1', 'value2', 'value3', 'value4')

**```tuple()```** is needed, if not, it will return a generator, for **```()```** is the grammar of generator

```python
{
new_tuple = (f(x) for x in list0)
print(type(new_tuple))
}
```

>\<class 'generator'>

#### (3) set derivation

Generate a set by derivation

```python
{
new_set = {f(x) for x in list0}
print(new_set)
}
```

>{'value1', 'value4', 'value3', 'value2'}

#### (4) dictionary derivation

Generate a dictionary by derivation

```python
{
new_dict = {f(x): x for x in list0}
print(new_dict)
}
```

>{'value1': 1, 'value2': 2, 'value3': 3, 'value4': 4}
