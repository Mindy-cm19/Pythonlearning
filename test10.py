# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender,Gender):
            self.gender = gender
        elif isinstance(Gender(gender),Gender):
            self.gender=Gender(gender)
        else:
            raise ValueError('只接受枚举类型参数')


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

bart = Student('Bart', 0)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
