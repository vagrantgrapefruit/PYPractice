# -*- coding: utf-8 -*-
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#字符转化为数字
def char2num(s):
    return DIGITS[s]
#字符串转化为浮点数
def str2float(s):
    Slist = s.split('.')
    if len(Slist)==1:
        return reduce(lambda x, y: x * 10 + y, map(char2num, Slist[0]))
    else:
        return reduce(lambda x, y: x * 10 + y, map(char2num, Slist[0]))+reduce(lambda x, y: x * 10  + y, map(char2num, Slist[1]))*10**(-len(Slist[1]))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')