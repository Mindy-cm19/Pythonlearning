# Python内置的@property装饰器负责把一个方法变成属性调用：
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s=Student()
s.score=60
s.score

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        self._width=width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height=height
    @property
    def resolution(self):
        return self._width*self._height

s=Screen()
s.width = 1024
s.height = 768
s.resolution