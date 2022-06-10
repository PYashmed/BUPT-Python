src_file = r"C:\Users\PYashmed\Desktop\BUPT\BUPTPython\Python\BUPTcourse\chapter7\file0.txt"
new_file = r"C:\Users\PYashmed\Desktop\BUPT\BUPTPython\Python\BUPTcourse\chapter7\file01.txt"
f = open(src_file, "r")
nf = open(new_file, "w")
# for line in f:
#     nf.write(line.replace("hello", "hallo"))

f.close()
nf.close()
