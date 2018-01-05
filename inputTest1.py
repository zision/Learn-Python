#身高输入测试
sex = str(input('请输入你的年龄(男/女)：'))
if sex == '男':
    tall = int(input('请输入你的身高(cm)：'))  # 转换输入为整数
    if tall < 160:
        print('你是小人国来的吧！')
    elif 160 <= tall < 180:
        print('一般的身高。')
    elif 180 <= tall < 185:
        print('王子般的身高！')
    elif 185 <= tall < 200:
        print('霸气侧漏！')
    elif 200 <= tall < 300:
        print('巨人般的身高！')
    else:
        print('你特么在逗我？重新输入！')
elif sex == '女':
    tall = int(input('请输入你的身高(cm)：'))
    if tall < 160:
        print('小萝莉来让叔叔抱抱~')
    elif 160 <= tall < 170:
        print('一般的身高。')
    elif 170 <= tall < 180:
        print('东京树！')
    elif 180 <= tall < 250:
        print('巨人般的身高！')
    else:
        print('你特么在逗我？重新输入！')
else:
    print('输错了，重新输入！')
