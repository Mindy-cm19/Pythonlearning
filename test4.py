# 假设Python没有提供int()函数，自己写一个把字符串转化为整数的函数。(map reduce)
from functools import reduce
digit={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2int(x):
    def cha2num(s):
        return digit[s]
    return reduce(lambda x,y : x*10 + y , map(cha2num,x))

str2int('135789')+1

# 练习1:利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper()+name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习2：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y : x*y , L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 练习3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
s='1237.456'
len(s)
s.index('.')
digit={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

# (1)只能用于有小数点存在时
def str2float(s):
    def chr2num(x):
        if x=='.':
            pass
        else:
            return digit[x]
    return reduce(lambda x,y : x*10 + y , filter(None,map(chr2num,s)))/(10**(len(s)-s.index('.')-1))

# (2)改进：用于所有字符串数字
def str2float(s):
    digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def chr2num(x):
        return digit[x]
    if '.' in s:
        return reduce(lambda x,y:x*10+y , map(chr2num,s.replace('.','')))*pow(10,s.index('.')+1-len(s))
    else:
        return reduce(lambda x,y:x*10+y , map(chr2num,s))