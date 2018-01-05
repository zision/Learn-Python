# 函数中变量的作用域
a = 0
# 全局变量，作用域为全局


def dayin_outer():
    a = 1
    # 局部变量，作用域为dayin_outer()外层函数中
    print('outer = %d' % a)

    def dayin_inner():
        a = 2
        # 局部变量，作用域为dayin_outer()内层函数中
        print('inner = %d' % a)
    dayin_inner()


print(a)
# 如果内层没有定义变量，则会取外层的变量值
dayin_outer()


# 匿名函数
jia_fa = lambda x, y: x+y
# 函数对象名 = lambda 形式参数：表达式
print(jia_fa(1, 2))


find_max = lambda x, y: x if x >= y else y
# 匿名函数的条件分支语句
print(find_max(1, 2))
# 函数复杂时不建议用匿名函数，结构复杂难以理解，PEP8也不推荐


# 函数的递归
'''斐波那契数列问题
1、新出生的小兔子在一个月的时间里发育为成年兔子；
2、每对成年兔子每月繁殖一对小兔子（雌雄一对）；
3、兔子没有死亡发生。　　
我们用Fn代表n个月后兔子的对数。
因为从一对新生的兔子开始，所以，F0=1，F1=1。
这一对兔子在第二个月末生出另一对小兔子，从而F2=1+1=2。
在第三个月末，第一对兔子将生下又一对小兔子，所以F3=2+1=3。
由此可知，从第一个月开始以后每个月的兔子总数是: 
1,1,2,3,5,8,13,21,34,55,89,144,233…　　
这就是著名的Fibonacci（斐波那契）数列

这个数列具有这样的特点：前两项均为1，从第三项起，每一项都是其前两项的和
即F0=F1=1，当n＞1时，Fn+2=Fn+1+Fn。
将其写成函数。
'''
def feb(n):
    if n <= 1:
        return 1
    else:
        return feb(n-1) + feb(n-2)


print(feb(0), feb(4), feb(10))
