# 文件处理

## 文件打开

+ python 打开文件使用`open()`函数
+ open()函数会返回一个对象，该对象为文件`<class '_io.TextIOWrapper'>`
+ 对返回的对象操作并不能直接更改文件，更改文件必须写入

```python
f = open(file_name,"access_mode","buffering",encoding="")
```

`file_name`文件名，可使用绝对路径（从盘到文件）或相对路径

`access_mode`访问模式
|模式|描述|
|--|--|
|r|只读|
|w|全新写入，文件不存在则创建|
|a|追加（不会覆盖），文件不存在则创建|
|+|可读可写|
|b|二进制格式，图片或视频需要设置b|
`r` `w` `a`为基础访问模式，`b` `+`是增加访问模式，使用时可将后者与前者结合，或单独使用前者。

例如：`rb+`二进制打开文件，可读可写，不存在不会创建。`wb+`二进制打开文件，可读可写，不存在则创建

`buffering`缓冲区设置
每一次IO操作都要调用CPU的IO指令，将内容写入磁盘，如果单次写入内容较少，会造成一定的资源浪费。设置缓冲区大小就像QQ聊天时，在聊天框输入，在发送前都不会执行IO操作。
|值|描述|
|--|--|
|>1|设置缓存大小（字节），缓存填满后执行一次IO|
|1|行缓冲，遇到换行符后IO|
|0|关闭缓冲，仅对二进制文件生效|
|-1(缺省)|默认缓冲8192(8k)|

## 文件对象

|属性|描述|
|-|-|
|closed|判断文件是否关闭|
|mode|文件的打开方式|
|newlines|换行模式|
|encoding|编码类型|
|name|文件名（实际上是地址）|

|方法|描述|
|-|-|
|file()|与open()函数类似，打开文件，（官方文档：最好不用）|
|close()|关闭文件|
|flush()|flush--冲洗，清理缓冲区，将缓存写入|
|read([size])|读取size个字节作为**字符串**返回|
|readline([size])|读取一行，将size字节内容作为**字符串**返回，缺省size则返回一整行，不包含换行符|
|readlines([size])|读取所有行，返回size字节，缺省则返回所有，包含换行符。[关于readlines的size判定](#readlines-1)|
|tell()|返回文件指针当前位置(不可与readlines,next(f)同时使用|
|seek(offset,[whence])|指针移动到新位置，`[whence]`可取`0` `1` `2`，`0`为从文件开头，`1`为从当前位置（仅二进制），`2`为从文件末尾（仅二进制）， `offset`相对起始位置的移动距离|
|truncate([size])|truncate--截断，保留size个字符，剩余内容删除|
|**next( f )**|注意是**函数**而不是方法，返回下一行内容，将光标移动到下一行|
|write(str)|将**字符串**写入|
|writelines([])|将**列表**中的字符遍历写入，没什么其他区别（和write）|

### readlines {#1}

`readlines([size])`方法关于size的判定如下

当取到第`i`行时，若包含换行符（1字节）的内容**不大于**（**可以是等于**）**`size`** *~~人间迷惑~~* 则继续向下取一行，每次返回不会截断一行，而会在列表内返回一整行。连续使用readlines会继续向下读取，而不是从头开始。

>**file**
123456
2345
6789

```python
print(f.readlines(6))
print(f.readlines(7))
```

>['123456\n']   （第一行包含换行符有七个字符，读取完整行）
['2345\n', '6789\n']   （从第二行继续读取，第二行包含五个字符，不大于size（==5），继续向下读取到第三行）

## 文件操作

### 文件读取

|方法|描述|
|-|-|
|read()|以二进制形式读取全部内容，返回内容需使用`str()`或`t.decode("utf-8)`来转换为字符串|

### 文件写入

### 文件删除

### 文件复制

### 文件重命名

### 文件内容搜索替换

#### 文件内容查找

1. 打开文件
2. 读取文件
3. 每一行里找（就是这么暴力）

```python
src_file = r"C:\Users\PYashmed\Desktop\BUPT\BUPTPython\Python\BUPTcourse\chapter7\file0.txt"
f = open(src_file, "r")
count = 0
for line in f:
    count += line.count("hello")

print(count)
```

>**file0.txt**
hello
hello hello hello
hello world
>count == 8

#### 文件内容替换

1. 重复查找步骤
2. 每一行里操作replace ~~（还是这么暴力）~~
3. 再把每一行写到一个新的文件里
4. 把之前文件删了 *~~暴力美学~~*

```python
src_file = r"C:\Users\PYashmed\Desktop\BUPT\BUPTPython\Python\BUPTcourse\chapter7\file0.txt"
new_file = r"C:\Users\PYashmed\Desktop\BUPT\BUPTPython\Python\BUPTcourse\chapter7\file01.txt"
f = open(src_file, "r")
nf = open(new_file, "w")
for line in f:
    nf.write(line.replace("hello", "hallo"))
f.close()
nf.close()
```

> **file01.txt**
> hallo
hallo hallo hallo
hallo world

### 文件比较
