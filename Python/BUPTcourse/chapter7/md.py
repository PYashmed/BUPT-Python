# -*-coding=utf-8-*-
import os
import shutil
src_file = r"C:\Users\PYashmed\Desktop\BUPT\BUPTPython\Python\BUPTcourse\chapter7\file0.txt"
new_file = r"C:\Users\PYashmed\Desktop\BUPT\BUPTPython\Python\BUPTcourse\chapter7\file01.txt"
new_file2 = r"C:\Users\PYashmed\Desktop\BUPT\BUPTPython\Python\BUPTcourse\chapter7\file02.txt"
src = open(src_file, 'r')
new = open(new_file, 'w')
# while True:
#     t = src.read(1)
#     if not t:
#         break
#     else:
#         new.write(t)
# t = src.read()
# new.write(t)

# for line in src:
#     new.write(line)
# shutil.copyfile(src_file, "new_file2.txt")


# dir1 = "Python/BUPTcourse/chapter7"
# l1 = os.listdir("Python/BUPTcourse/chapter7")
# for file in l1:
#     l2 = os.path.splitext(file)
#     print(l2)
# print(l1)


# if 'file02.txt' in l1:
#     os.rename(dir1+"/file02.txt", dir1+"/file2.txt")
# elif "file2.txt" in l1:
#     os.rename(dir1+"/file2.txt", dir1+"/file02.txt")


# f = open(src_file, "r", encoding="utf-8")
# for line in f:
#     print(line, end="")

# print(f.readline())
# print(f.readline())
# print(f.readlines())
# data = f.read()
# 如果是二进制
# print(str(data))
# print(data.decode("utf-8"))
# print(data)
# nf = open(new_file, "w")
# for line in f:
#     nf.write(line.replace("hello", "hallo"))


os.mkdir("Python/BUPTcourse/chapter7/dir1111")
os.makedirs("Python/BUPTcourse/chapter7/dir111/dir222")
