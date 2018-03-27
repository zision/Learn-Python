# -*- coding: utf-8 -*-
# 适用于Python2.7
# 几种排序算法的Python实现
import random
import time
from functools import wraps
import sys


# 计时装饰器
def fn_timer(fn):
    @wraps(fn)
    def function_timer(*args, **kwargs):
        t0 = time.clock()
        result = fn(*args, **kwargs)
        t1 = time.clock()
        print ("函数'%s'本次运行耗时: %s 秒" %
               (fn.func_name, str(t1-t0))
               )
        return result
    return function_timer


# 输入一个整数n，随机生成一个包含n个元素的list
def get_random(num):
    a = []
    i = 0
    while i < num:
        a.append(random.randint(0, 10000))
        i += 1
    return a


# 直接插入排序
@fn_timer
def insert_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    return array


# 冒泡排序
@fn_timer
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


# 快速排序
def quick_sort(array):
    sys.setrecursionlimit(10000)
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        small = [i for i in array[1:] if i < pivot]
        big = [i for i in array[1:] if i > pivot]
    return quick_sort(small) + [pivot] + quick_sort(big)


# 输出测试
if __name__ == '__main__':
    list1 = get_random(int(input('输入随机生成列表长度:')))
    print('原列表为:%s\n' % list1)
    t0 = time.clock()
    print('冒泡排序后:%s\n冒泡排序耗时:%s秒\n' % (bubble_sort(list1), time.clock()-t0))
    t0 = time.clock()
    print('插入排序后:%s\n插入排序耗时:%s秒\n' % (insert_sort(list1), time.clock()-t0))
    t0 = time.clock()
    print('快速排序后:%s\n快速排序耗时:%s秒\n' % (quick_sort(list1), time.clock()-t0))

