# coding=utf-8
# 牛课网空格分割标准输入, Python2.7
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



# 标准输出
if __name__ == '__main__':
    try:
        print(str_l)
        print(int_l)
    except:
        pass

