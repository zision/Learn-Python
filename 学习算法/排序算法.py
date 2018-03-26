# coding=utf-8


# 牛课网专用空格分割输入, 适用于Python2.7
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        str_l = line.split()
        int_l = list(map(int, line.split(' ')))
except:
    pass


# 快速排序
try:
    n = len(int_l)
    

# 标准输出
try:
    print(str_l)
    print(int_l)
except:
    pass
