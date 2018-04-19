# -*- coding: utf-8 -*-

import re

line = 'booooooooooobby123'
regex_str = '^b.*3$'
if re.match(regex_str, line):
    print('yes')
    regex_str = ".*?(b.*?b).*"  # 非贪婪匹配与贪婪匹配
    match_obj = re.match(regex_str, line)
    print(match_obj.group(1))
else:
    print('no')
