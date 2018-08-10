#生成器
print([i for i in range(5)])
print(i for i in range(5))

"""
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator.
"""
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'Done!'

print(fib(6))

for i in fib(5):
    print(i)

"""
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中。
"""
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:%i' %x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break


#练习：杨辉三角
def triangles():
    a=[]
    b=[1]
    while True:
        yield b
        a=[0]+b+[0]
        b=[a[i]+a[i+1] for i in range(len(a)-1)]

n=0
for t in triangles():
    print(t)
    n+=1
    if n == 10:
        break