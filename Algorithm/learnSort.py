# -*- coding: utf-8 -*-
# 适用于Python2.7
# 几种排序算法的Python实现
import copy
import random
import time
from functools import wraps
import sys


sys.setrecursionlimit(100000)


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


# 第一种快速排序
def quick_sort1(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        small = [i for i in array[1:] if i < pivot]
        big = [i for i in array[1:] if i >= pivot]
    return quick_sort1(small) + [pivot] + quick_sort1(big)


# 第二种快速排序写法,更高效
def quick_sort2(array):
    def recursive(begin, end):
        if begin > end:
            return
        l, r = begin, end
        pivot = array[l]
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l - 1)
        recursive(r + 1, end)

    recursive(0, len(array) - 1)
    return array


'''
# 还没想好怎么写
def quick_sort3(array):
    left = 0
    right = len(array) - 1
    if left >= right:
        return array
    else:
        key = array[0]
        while left < right and array[right] >= key:
            right -= 1
        while left < right and array[left] < key:
            left += 1
        array[left], array[right] = array[right], array[left]
        return array
'''

# 输出测试
if __name__ == '__main__':
    list1 = get_random(int(input('输入随机生成列表长度:')))
    print('原列表为:%s\n' % list1)
    t0 = time.clock()
    print('Py自带排序后:%s\nPy自带排序耗时: %s秒\n' % (sorted(copy.copy(list1)), time.clock()-t0))
    t0 = time.clock()
    print('冒泡排序后:%s\n冒泡排序耗时: %s秒\n' % (bubble_sort(copy.copy(list1)), time.clock()-t0))
    t0 = time.clock()
    print('插入排序后:%s\n插入排序耗时: %s秒\n' % (insert_sort(copy.copy(list1)), time.clock()-t0))
    t0 = time.clock()
    print('快速排序1后:%s\n快速排序1耗时: %s秒\n' % (quick_sort1(copy.copy(list1)), time.clock()-t0))
    t0 = time.clock()
    print('快速排序2后:%s\n快速排序2耗时: %s秒\n' % (quick_sort2(copy.copy(list1)), time.clock()-t0))
    print(list1)
