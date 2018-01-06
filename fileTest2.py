# 文件的编码
'''Python3.X版本，在这个版本中，文件默认的编码方式就是utf-8
文本字符的常用的编码有ASCII和Unicode
值得注意的是，在Python3.X中，字符串等所有的文本字符使用的是unicode编码，
可以使用encode（）进行编码为utf-8
使用decode（）可以将utf-8文件解码为文本字符'''
s = '周子健正在学习Python'
s.encode()
