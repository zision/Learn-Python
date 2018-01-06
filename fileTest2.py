# 文件的编码
'''Python3.X版本，在这个版本中，文件默认的编码方式就是utf-8
文本字符的常用的编码有ASCII和Unicode
值得注意的是，在Python3.X中，字符串等所有的文本字符使用的是unicode编码，
可以使用encode（）进行编码为utf-8
使用decode（）可以将utf-8文件解码为文本字符'''
s = '周子健正在学习Python'
print(s.encode())
print(s.encode('gbk'))
s1 = s.encode()
print(s1.decode())  # 将utf-8解码回来
# print(s1.decode('gbk'))  # utf-8使用gbk解码会报错
s2 = s.encode('gbk')
print(s2.decode('gbk'))  # 将gbk解码回来

print(type(s))
print(type(s1))
print(type(s2))


# 文件的打开和关闭
'''Python对文件的操作有文件打开、文件内容读取、文件修改、文件关闭等
使用open（）来打开文件
使用方式如下：
文件对象 = open（文件名 [，模式 ]）
模式是可选参数，通常有以下几种：

w     以写方式打开，如果这个文件不存在，则创建这个文件
r      以只读方式打开
a     以写方式打开，写的内容追加在文章末尾（像列表的append（））
b     表示二进制文件
+     以修改方式打开，支持读/写
r+    以读写模式打开
w+   以读写模式打开 (参见 w )
a+    以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb    以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+   以二进制读写模式打开 (参见 r+ )
wb+  以二进制读写模式打开 (参见 w+ )
ab+  以二进制读写模式打开 (参见 a+ )

怎么记住呢？
w = write 写
r = read 读
b = bytes 二进制
a = append 追加
然后可能组合一下

如果不加模式，默认的是 r

处理完一个文件时候，要关闭文件
'''
f = open('fileTest2.txt', 'w')
f.close()


# 文件写入
f = open('fileTest2.txt', 'a')
f.write('我先添加一行文字，这里没有用import os指定路径。')
f.close()
f = open('fileTest2.txt', 'a')
f.write('\n我再添加一行文字，依旧没有指定路径。')
f.close()

import os
os.chdir('D:\GitHub\PyPractice')
f = open('fileTest2.txt')
print(f.read())
f.close()

f = open('fileTest2.txt')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open('fileTest2.txt')
for i in range(0, 2):
    print(f.readline())
# 但是一般情况不知道会有多少行
f.close()


f = open('fileTest2.txt')
for i in f.readlines():
    print(i)
f.close()