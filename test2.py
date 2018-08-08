"""
练习：请使用迭代查找一个list中最小和最大值，并返回一个tuple：
"""

# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L==[]:    
        return (None, None)
    else:
        min=L[0]
        max=L[0]
        for i in L:
            if i<min:
                min=i
            elif i>max:
                max=i
        return (min, max)
