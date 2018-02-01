# -*- coding: utf-8 -*-

def normalize(name):
    return name.title()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)