# -*- coding: utf-8 -*-
# 适用于Python2.7
# 几种排序算法的Python实现
import random
import time
from functools import wraps


# 计时装饰器
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.clock()
        result = function(*args, **kwargs)
        t1 = time.clock()
        print ("函数'%s'本次运行耗时: %s 秒" %
               (function.func_name, str(t1-t0))
               )
        return result
    return function_timer


# 输入一个整数n，随机生成一个包含n个元素的list
def get_random(num):
    a = []
    i = 0
    while i < num:
        a.append(random.randint(0, 1000))
        i += 1
    return a


# 冒泡排序
@fn_timer
def bubble_sort(buli):
    for i in range(len(buli)-1):
        for j in range(len(buli)-i-1):
            if buli[j] > buli[j+1]:
                buli[j], buli[j+1] = buli[j+1], buli[j]
    return buli


# 输出测试
if __name__ == '__main__':
    list1 = get_random(int(input('输入随机生成列表长度:')))
    print('原列表为:%s' % list1)
    print('冒泡排序后:%s' % bubble_sort(list1))


