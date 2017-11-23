class Student(object):
    # __slots__ = ('name', 'age', 'score','__name')  # 用tuple定义允许绑定的属性名称
    @property
    def age(self):
        return self._age
    @age.setter # 如果不写setter方法，那么age就是一个只读的属性了
    def age(self, value):
        if not isinstance(value,int):
            raise  ValueError('age must be an integer!')
        if value < 0 or value > 150:
            raise  ValueError('age must between 0 ~ 150!')
        self._age = value



    # 加上__私有化
    def __init__(self,name,score):
        self.__name = name
        self.score = score
    def getScore(self):
        print(self.__name,self.score)
        return self.score
    def getName(self):
        print(self.__name,self.score)
        return self.__name

    pass

bart = Student('Minyahui',100)
bart.age = 120
print(bart.age)
# bart._Student__name 访问私有的变量
print(bart.score,bart._Student__name)
print(type(bart))