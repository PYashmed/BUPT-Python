# �ļ�����

## �ļ���

+ python ���ļ�ʹ��`open()`����
+ open()�����᷵��һ�����󣬸ö���Ϊ�ļ�`<class '_io.TextIOWrapper'>`
+ �Է��صĶ������������ֱ�Ӹ����ļ��������ļ�����д��

```python
f = open(file_name,"access_mode","buffering",encoding="")
```

`file_name`�ļ�������ʹ�þ���·�������̵��ļ��������·��

`access_mode`����ģʽ
|ģʽ|����|
|--|--|
|r|ֻ��|
|w|ȫ��д�룬�ļ��������򴴽�|
|a|׷�ӣ����Ḳ�ǣ����ļ��������򴴽�|
|+|�ɶ���д|
|b|�����Ƹ�ʽ��ͼƬ����Ƶ��Ҫ����b|
`r` `w` `a`Ϊ��������ģʽ��`b` `+`�����ӷ���ģʽ��ʹ��ʱ�ɽ�������ǰ�߽�ϣ��򵥶�ʹ��ǰ�ߡ�

���磺`rb+`�����ƴ��ļ����ɶ���д�������ڲ��ᴴ����`wb+`�����ƴ��ļ����ɶ���д���������򴴽�

`buffering`����������
ÿһ��IO������Ҫ����CPU��IOָ�������д����̣��������д�����ݽ��٣������һ������Դ�˷ѡ����û�������С����QQ����ʱ������������룬�ڷ���ǰ������ִ��IO������
|ֵ|����|
|--|--|
|>1|���û����С���ֽڣ�������������ִ��һ��IO|
|1|�л��壬�������з���IO|
|0|�رջ��壬���Զ������ļ���Ч|
|-1(ȱʡ)|Ĭ�ϻ���8192(8k)|

## �ļ�����

|����|����|
|-|-|
|closed|�ж��ļ��Ƿ�ر�|
|mode|�ļ��Ĵ򿪷�ʽ|
|newlines|����ģʽ|
|encoding|��������|
|name|�ļ�����ʵ�����ǵ�ַ��|

|����|����|
|-|-|
|file()|��open()�������ƣ����ļ������ٷ��ĵ�����ò��ã�|
|close()|�ر��ļ�|
|flush()|flush--��ϴ������������������д��|
|read([size])|��ȡsize���ֽ���Ϊ**�ַ���**���أ�Ĭ�϶�ȡȫ��|
|readline([size])|��ȡһ�У���size�ֽ�������Ϊ**�ַ���**���أ�ȱʡsize�򷵻�һ���У����������з�|
|readlines([size])|��ȡ�����У�����size�ֽڣ�ȱʡ�򷵻����У��������з���[����readlines��size�ж�](#readlines-1)|
|tell()|�����ļ�ָ�뵱ǰλ��(������readlines,next(f)ͬʱʹ��|
|seek(offset,[whence])|ָ���ƶ�����λ�ã�`[whence]`��ȡ`0` `1` `2`��`0`Ϊ���ļ���ͷ��`1`Ϊ�ӵ�ǰλ�ã��������ƣ���`2`Ϊ���ļ�ĩβ���������ƣ��� `offset`�����ʼλ�õ��ƶ�����|
|truncate([size])|truncate--�ضϣ�����size���ַ���ʣ������ɾ��|
|**next( f )**|ע����**����**�����Ƿ�����������һ�����ݣ�������ƶ�����һ��|
|write(str)|��**�ַ���**д��|
|writelines([])|��**�б�**�е��ַ�����д�룬ûʲô�������𣨺�write��|

***ע�⣺û�� `writeline()`����***

### readlines {#1}

`readlines([size])`��������size���ж�����

��ȡ����`i`��ʱ�����������з���1�ֽڣ�������**������**��**�����ǵ���**��**`size`** *~~�˼��Ի�~~* ���������ȡһ�У�ÿ�η��ز���ض�һ�У��������б��ڷ���һ���С�����ʹ��readlines��������¶�ȡ�������Ǵ�ͷ��ʼ��

>**file**
123456
2345
6789

```python
print(f.readlines(6))
print(f.readlines(7))
```

>['123456\n']   ����һ�а������з����߸��ַ�����ȡ�����У�
['2345\n', '6789\n']   ���ӵڶ��м�����ȡ���ڶ��а�������ַ���������size��==5�����������¶�ȡ�������У�

## �ļ�����

### �ļ���ȡ

#### ��ȡȫ������

|����|����|
|-|-|
|read()|���Զ�������ʽ��ȡȫ������(b)������������ʹ��`str()`��`t.decode("utf-8)`��ת��Ϊ�ַ���|

ʵ���߼���

+ ���ļ�
+ ��ȡ�ļ�����

```python
f = open(src_file, "r")
data=f.read()
# ����Ƕ�����
print(str(data))
print(data.decode("utf-8"))
print(data)
```

#### ��ȡ��

|����|����|
|-|-|
|readline()|��ȡһ�����ݣ������ַ���������ʾ���з�����**����**���з�����������print(f.readline())����ִ�������,��[��������](#��������-3)��|
|readlines()|��ȡ���������ݣ�����ΪԪ�ش�Ϊ�б��������з�`\n`|
|[���󺭸�](#���󺭸Ƕ�ȡ-2)|ʹ��forѭ�������ļ����Ͷ����ڵ�Ԫ��|

***`readline()`��`readlines()`����ָ��λ��***��ȡʱ��������ȡ�����ظ���ȡ

```python
f = open(src_file, "r", encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readlines())
```

>file0.line0
>
>file0.line1
>
>['file0.line2\n', 'file0.line3\n', 'file0.line4\n', 'file0.line5\n', 'file0.line6\n']

##### ���󺭸Ƕ�ȡ {#2}

```python
f = open(src_file, "r", encoding="utf-8")
for line in f:
    print(line)
```

>file0.line0
>
>file0.line1
>
>file0.line2
>
>file0.line3
>
>file0.line4
>
>file0.line5
>
>file0.line6

##### �������� {#3}

���ڷ��ص��ַ����������Ƿ���ʾ���з�`\n`�������ǰ������з������Ҫ�������˷��յĴ����Ŀ��У�ֻ��Ҫ��`print()`��ʹ��`end=""`

```python
f = open(src_file, "r", encoding="utf-8")
for line in f:
    print(line, end="")
```

>file0.line0
file0.line1
file0.line2
file0.line3
file0.line4
file0.line5
file0.line6

### �ļ�д��

|����|����|
|-|-|
|write()|д���ַ����������ֶ�д�뻻�з������Զ����Ʋ����ļ�����(wb/ab)�������д��������ַ�|
|writelines()|�����б�д�룬���ֶ�д�뻻�з��������ַ�������Ϊ�����Ч��|

### �ļ�ɾ��

|ģ��|����|����|
|:-:|:-:|:-:|
|os|os.remove(file_name)|ɾ���ļ����ļ��������򱨴�|
|os|os.path.exists(file_name)|�ж��ļ��Ƿ���ڣ�`bool`|

### �ļ�����

#### ��������read--wrute

+ ��ȡ����
+ д������~~���Ǳ�����ѧ~~

PPT������ֵķ��� ��

```python
while True:
    t = src.read(1)
    if not t:
        break
    else:
        new.write(t)
```

��������Ҳ��....

```python
t = src.read()
new.write(t)
```

#### �����ļ�����Ԫ�� ~~���Ǳ���~~

+ һ��һ��д�¡�����

```python
for line in src:
    new.write(line)
```

#### shutilģ�� ��������

|ģ��|����|����|
|:-:|:-:|:-:|
|shutil|shutil.copyfile(src_file,new_file)|���ƣ����Ҵ���, �������ļ����Լ��½�|

+ `new_file`������**��ַ**Ҳ������**�ļ���**��ע��Ҫ����׺��������������ַ����**��ǰ������**�¼��������������½��ļ�

### �ļ�����

|ģ��|����|����|
|:-:|:-:|:-:|
|shutil|shutil.move(src_file,new_file)|��copyfile���ƣ�ֻ������`ctrl+x`��Ч��|

### �ļ�������

|ģ��|����|����|
|:-:|:-:|:-:|
|os|os.rename(old_name,new_name)|��ʵ����Ҫ����ȥ����·��|
|os|os.listdir(dir_name)|��ȡ`dir_name`Ŀ¼�µ��ļ�������ȷ��Ҫ���������ļ���ָ�����б��ڣ������б����|

+ �ӹ�������Ŀ¼����
+ �����ϳ���������(./)
+ һ�����м���ٽ��и���

```python
dir1 = "Python/BUPTcourse/chapter7"
l1 = os.listdir("Python/BUPTcourse/chapter7")
if 'file02.txt' in l1:
    os.rename(dir1+"/file02.txt", dir1+"/file2.txt")
elif "file2.txt" in l1:
    os.rename(dir1+"/file2.txt", dir1+"/file02.txt")
```

#### ���Һ�׺��

+ ��ʵ��`os.rename()`�Ϳ�������
+ ��һ����

|ģ��|����|����|
|:-:|:-:|:-:|
|os|os.path.splitext(file)|�����ļ������ֺͺ�׺����Ԫ�飬�ļ��к�׺Ϊ��|

```python
dir1 = "Python/BUPTcourse/chapter7"
l1 = os.listdir("Python/BUPTcourse/chapter7")
for file in l1:
    l2 = os.path.splitext(file)
    print(l2)
```

>('file0', '.txt')
('file01', '.txt')
('file02', '.txt')

### �ļ����������滻

#### �ļ����ݲ���

1. ���ļ�
2. ��ȡ�ļ�
3. ÿһ�����ң�������ô������

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

#### �ļ������滻

1. �ظ����Ҳ���
2. ÿһ�������replace ~~��������ô������~~
3. �ٰ�ÿһ��д��һ���µ��ļ���
4. ��֮ǰ�ļ�ɾ�� *~~������ѧ~~*

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

### �ļ��Ƚ�

## Ŀ¼����

|����|����|
|:-:|:-:|
|os.mkdir(path)|����һ��Ŀ¼�����ܴ����Ѵ���Ŀ¼��Ĭ�ϴӹ�������Ŀ¼��ʼ|
|os.makedirs(path)|`path`��Ҫ����༶Ŀ¼��ʽ`.../.../.../`�������༶Ŀ¼�������ظ���������Ŀ¼��Ĭ�ϴӹ�������Ŀ¼��ʼ|
|os.rmdir(path)|ɾ��Ŀ¼������ο�mkdir|
|os.removedirs(path)|ɾ���༶Ŀ¼|
|os.listdir(path)|���path�������ļ����������ļ���|
|os.getcwd()|��õ�ǰĿ¼|
|os.chdir(path)|���ĵ�ǰĿ¼��`path`|
|os.walk(top,topdown,onerroe,followlinks)

```python
os.mkdir("Python/BUPTcourse/chapter7/dir1111")
os.makedirs("Python/BUPTcourse/chapter7/dir111/dir222")
```
