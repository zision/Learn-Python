# 异常处理，用一个除法计算器演示
try:
    x = float(input('请输入被除数：'))
    y = float(input('请输入除数：'))
    z = x/y
    print(z)
except ZeroDivisionError:
    print('除数不能为0！')
except ValueError:
    print('只能输入数值类型！')
except:
    print('未知的错误！')
finally:
    print('无论如何我都能被打印出来！')