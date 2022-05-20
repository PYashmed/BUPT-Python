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
|    8     | `|`              | `0 | 0=0` `1 | x=1` |

### 3.1.5 number variable

