# Data

## 3.1 Number

### 3.1.1 essential number

#### (1) int float (omit)

#### (2) scientific notation

Example: `xey` or `xEy`, x = any, y (int)
Type of scientific notation is float

```python
print(3e-2, type(3e-2))
```

>0.03 \<class 'float'>

### 3.1.2 complex number

Like: `a+bj`

+ In python, imaginary part unit is `j`
+ Type of `a` and `b` must be  int or float
+ If `b == 1`, `1` cannot be skipped over

### 3.1.3 system

#### (1) basic system

| system      | format        | example |
| ----------- | ------------- | ------- |
| binary      | `0byy` `0Byy` | 0b11    |
| octonary    | `0oyy` `0Oyy` | 0O77    |
| hexadecimal | `0xyy` `0Xyy` | 0xc8    |

`yy` on behalf of any number, not double_digit

#### (2) system conversion

| From\To | binary   | octonary | hexadecimal |
| ------- | -------- | -------- | ----------- |
| decimal | `bin(x)` | `oct(x)` | `hex(x)`    |

### 3.1.4 arithmetic operator

| Priority | Operator         | Describe                            |
| :------: | ---------------- | ----------------------------------- |
|    20    | `()`             | boost the priority                  |
|    16    | `**`             | index `2**2=4`                      |
|    15    | `~`              | `0->1` `1->0` `~a=-(a+1)`           |
|    14    | `+x` `-x`        | plus-minus sign                     |
|    13    | `*` `/` `//` `%` | `3*4=12` `5/2=2.5` `5//2=2` `5%2=1` |
|    12    | `+` `-`          | plus and minus                      |
|    11    | `<<` `>>`        | `a<<b=a*2b` `a>>b=a//2b`            |
|    10    | `&`              | `1&1=1` `0&x=0`                     |
|    9     | `^`              | `0^1=1` `1^0=1` `0^0=0` `1^1-0`     |
|    8     | `                | `                                   | `0 | 0=0` `1 | x=1` |

### 3.1.5 number variable

numerical object is **immutable**, two variable with the same value point to the same address

```python
a = 1
b = 1
print(id(a), id(b))
```

>2858153830704 2858153830704

variable is an index, point to the object's address, if give the variable a new value, the address the variable pointed to will change

```python
a = 1
print(id(a))
a = 2
print(id(a))
```

>2237494618416
2237494618448

### 3.1.6 basic numerical function

#### (1) int()

Convert **`int`** **`float`** **`str(int)`** to **`int`**
`Float` is converted to `int` by discarding the decimal part

```python
print(type(int(10)), type(int(10.3)), type(int("101")))
```

>\<class 'int'> \<class 'int'> \<class 'int'>

```python
print(type(int('A')))
print(type(int(1+2j)))
```

>ValueError: invalid literal for int() with base 10: 'A'
TypeError: can't convert complex to int

#### (2) float()

Convert **`int`** **`float`** **`str(float)`** to **`float`**

