# -*-coding=utf-8-*-
l1=[(1,2),0]
t1=([1,2],0)
print(t1,id(t1[0]))
t1[0][1]=1
print(t1,id(t1[0]))