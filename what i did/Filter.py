# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x: x % n > 0        
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
# # 打印1000以内的素数:
# for n in primes():
#     if n < 10:
#         print(n)
#     else:
#         break
    ##-----------------------------------------------------------------------
# -*- coding: utf-8 -*-

##判断回文数字/字符串
def is_palindrome(n):
    s=str(n)
    i=len(s)//2
    n=0
    while n<i:        
        if s[n]==s[-1-n]:
            n=n+1
            continue
        else:
            return False
    return True


# 测试:
output = filter(is_palindrome, range(1, 10000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')