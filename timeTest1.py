import time

print(time.time())  # 从1970年1月1日午夜至今的时间

print(time.localtime())  # 当前时间信息

print(time.mktime(time.localtime()))  # 转为时间戳

t = time.mktime(time.localtime())
print(time.asctime(time.localtime()))  # 转换为一般容易识别的时间形式
print(time.ctime(t))  # 将时间戳转换为容易识别的时间形式

a = time.strftime('%Y-%m-%d %X', time.localtime())
print(a)
# 自行设定输出字符串的格式

print(time.strptime('2018-01-06 22:46:24', '%Y-%m-%d %X'))
# 逆向操作


time.sleep(1)  # 先休息1秒
for i in range(1, 10):
    print(i)
    time.sleep(0.1)
    # 每隔一秒打印一次


# 定义一个计时用函数
def usetime(f):
    def fn(*args, **kw):
        start = time.clock()
        r = f(*args, **kw)
        end = time.clock()
        print('call', f.__name__+'() in %ds' % (end-start))
        return r
    return fn


@usetime
def factorial(n):
    m = 1
    for i in range(1, n+1):
        m = m*i
    return m


print(factorial(10))
print(factorial(1000))
