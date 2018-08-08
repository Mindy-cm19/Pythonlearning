"""
写一个 可接收一个或多个数并计算乘积 的函数
"""

def product(*args):
    if len(args)== 0:
        raise TypeError('不能没有参数输入!')
    else:
        s=1
        for i in args:
            s=s*i
        return s
