#用for循环输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        q = i*j
        print(str(i)+'*'+str(j),'= %d'%q,end='  ')
    print('\n')

#break尝试
i = 0
while 1:
    print('这是第%d次循环'%i)
    i += 1
    if i > 10:
        break

#编写一个最多猜10次数字的游戏，猜测范围1~100，根据input内容提示猜大或者猜小，如果猜中，结束循环
import random
number = random.randint(1,100)
game = 0
for i in range(0,10):
    tryNum = int(input('第%d/10次尝试,您的猜测值为(1~100)：'%i))
    if 1 <= tryNum <= 100:
        if tryNum == number:
            game = 1
            break
        elif tryNum > number:
            print('猜大了。')
        else:
            print('猜小了。')
    else:
        print('十分抱歉，超出输入范围，你浪费了一次机会。')
if game == 1 :
    print('恭喜您猜中啦！用了%d次。' % i)
else:
    print('你失败了,答案为%d'%number)
