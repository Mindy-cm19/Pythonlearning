# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    a = [0]
    def counter():
        a[0] = a[0] + 1
        return a[0]
    return counter

# 参考：https://www.cnblogs.com/JohnABC/p/4076855.html