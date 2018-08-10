# 用filter求素数
"""
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 5,  7,  9,  11,  13,  15,  17,  19,  ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5,  7, 8,  10, 11, 13, 14,  16, 17,  19, 20, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 8, 9,  11, 12, 13, 14,  16, 17, 18, 19,  ...
不断筛下去，就可以得到所有的素数。
"""
# 首先定义一个不能整除则返回True的函数
def _not_divisible(n):
    return lambda x : x % n > 0
# 然后构造一个从3开始的奇数数列
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        it=filter(_not_divisible(n),it)
        yield n
# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break



# 练习：回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    strn=str(n)
    return strn==strn[::-1]

list(filter(is_palindrome,range(1000)))

