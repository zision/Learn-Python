print('Python'+'is'+'my'+'life')
print('Python' 'is' 'my' 'life')
print('Python''is''my''life')
print('Python','is','my','life')
print('Python'+' '+'is'+' '+'my'+' '+'life')

string = 'Python'
print(string[0],string[2],string[-1])
print(string[1:4])
print(string[1:4:2])
print(string[::])
print(string[2:])
print(string[::2])
print(string[::-1])
print(string[:5])
print(string[7:])
print(string[:8])
print('\r')
print(6**666)
print(int(9.99999))
print('10除以3的商和余数分别为',divmod(10,3))
print('12的二进制、八进制和十六进制分别为',bin(12),oct(12),hex(12))
print('3.4和3.5的四舍五入结果分别为',round(3.4),round(3.5))

import math
print('π和e的和为',math.pi + math.e)
from math import *
print('π和e的和=',pi + e)


#格式化操作符
number = 23333
print('前空格宽度6右对齐='+'%6d'%number)
print('宽度3按实际宽度输出='+'%3d'%number)
print('后空格宽度6左对齐='+'%-6d'%number)
print('带+左补全宽度6输出='+'%+6d'%number)
print('带0左补全宽度6输出='+'%06d'%number)
print('八进制形式输出='+'%#o'%number)
print('十六进制形式输出='+'%#x'%number)

#尝试使用str.format()格式化操作函数')
print('{name}今年{age}岁，啊，{age}!好一个如花的年龄!'.format(name='周子健',age=21))

#关系运算符
print(2>3,2<2.33,2<=3,2==3,True==1,True<2,False==0,True-False,True*2.33,2==2,2==3,2!=3,2!=2,2 is 2,2 is not 3)
a = 2
b = 2
print(a == b,a is b)
c = 2.0
print(a == c,c == a,a is c,c is a)
print(id(a),id(b),id(c))
#字符串的关系运算
print('zhouzijian1996' > 'zhouzijian')
print('abcd' < 'abdc')
print('' < 'a')
print('abcd' < 'd')
a = 0.1+0.2+0.3
print(a,a == 0.6,round(a,2) == 0.6)   #浮点数精度问题，转换二进制运算时无法完美保留,可用保留几位小数解决
#关于ASCII码的比较
print('0'<'A','a'<'A','a'<'哈哈')

#复合赋值语句
a,b = 2,'a'
print(a,b)
a,b,c,d,e,f = 'Python'
print(f,e,d,c,b,a)
f,e,d,c,b,a = a,b,c,d,e,f
print(f,e,d,c,b,a)


print(type('hello world!'))