# -*- coding: utf-8 -*-

import re

line = 'booooooobbbooooabby123'
regex_str = '^b.*3$'
if re.match(regex_str, line):
    print('yes')
    regex_str = ".*?(b.{2,8}?b).*"  # 非贪婪匹配与贪婪匹配
    match_obj = re.match(regex_str, line)
    print(match_obj.group(1))
else:
    print('no')


line = 'boobby123'
regex_str = "((bobby|boobby)123)"   # |表示或的关系
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

line = 'bobby123'
regex_str = "([abcd]obby123)"   # []表示括号内的任意字符均可匹配
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))


line = '18513851340'  # 手机号判断
regex_str = "(1[34578][0-9]{9})"   # 以1开头，0-9的数字出现9次
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1)+'是合法的手机号码')
else:
    print(line+'不是合法的手机号码！')
# [^1]代表不是1的字符

line = '你 好'
# line = '你嘿嘿好'
regex_str = "(你\s好)"   # \s代表空格，\S代表不是空格
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1), '第一种匹配成功')

regex_str = "(你\w好)"  # \w 代表[A-Za-z0-9_]的任意字符，\W大写表示\w的补集
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1), '第二种匹配成功')

regex_str = "(你\S+好)"   # \S+代表非空格且大于一次都可以匹配
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1), '第三种匹配成功')


line = "study in 上海交通大学"
regex_str = ".*?([\u4E00-\u9FA5]+大学)"   # .*代表前面任意多字符, ?代表非贪婪匹配, [\u4E00-\u9FA5]代表任意汉字, +代表任意多个
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1), '大学名称提取成功!')

line = "XXX出生于2001年"
regex_str = ".*?(\d+)年.*"   # \d代表数字 使用非贪婪或{4}限定提取4位均可
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1), '出生年份提取成功!')


# 提取出生日期实例
line = "XXX出生于2001年6月1日"
# line = "XXX出生于2001/6/1"
# line = "XXX出生于2001-6-1"
# line = "XXX出生于2001-06-01"
# line = "XXX出生于2001/06/01"
# line = "XXX出生于2001/06"

regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]$|[月/-]\d{1,2}$|[月/-]\d{1,2}日$|$))"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
