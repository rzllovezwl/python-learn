# 继承的语法
# 在python中，任何类都有一个共同的父类叫object
class Person():
    name = 'NoName'
    age = 0
    __score = 0 #考试成绩是秘密，只要自己知道
    _petname = 'chaolin' #小名，是受保护的，子类可以用，但不能公用
    def sleep(self):
        print('Sleeping.....')

# 父类写在括号内
class Teacher(Person):
    teacher_id = 9999
    def make_test(self): #子类可以拥有单独的属性
        print('zhuyi')

t = Teacher()
print(t.name)
print(t._petname) #可访问
# print(t.__score) #不可访问私有成员
t.sleep()
print(t.teacher_id)
t.make_test()

print('-' * 70)

# 子类和父类定义同一个变量名称，则优先使用子类本身
class Person():
    name = 'NoName'
    age = 0
    __score = 0 #考试成绩是秘密，只要自己知道
    _petname = 'chaolin' #小名，是受保护的，子类可以用，但不能公用
    def sleep(self):
        print('Sleeping.....')

# 父类写在括号内
class Teacher(Person):
    name = 'wenli'
    teacher_id = 9999
    def make_test(self): #子类可以拥有单独的属性
        print('zhuyi')

t = Teacher()
print(t.name)

print('-' * 70)

# 子类扩充父类功能的案例
# 人有工作的函数，老师也有工作的函数，但老师的工作需要讲课
class Person():
    name = 'NoName'
    age = 0
    __score = 0 #考试成绩是秘密，只要自己知道
    _petname = 'chaolin' #小名，是受保护的，子类可以用，但不能公用
    def sleep(self):
        print('Sleeping.....')
    def work(self):
        print('make some money')

# 父类写在括号内
class Teacher(Person):
    name = 'wenli'
    teacher_id = 9999
    def make_test(self): #子类可以拥有单独的属性
        print('zhuyi')

    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        Person.work(self)
        self.make_test()
        # 扩充父类的另一种方法
        # super代表得到父类
        super().work()
        print('xixi')

t = Teacher()
t.work()

print('-' * 70)

# 构造函数的概念

class Dog():
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('i am init in dog')
# 实例化的时候，括号内的参数需要跟构造函数参数匹配
kaka = Dog()

print('-' * 70)

# 继承中的构造函数：1
class Animel():
    pass
class PaxingAni(Animel):
    pass
class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('i am init in dog')
# 实例化的时候，自动调用了Dog的构造函数
kaka = Dog()

print('-' * 70)
# 继承中的构造函数：2

class Animel():
    def __init__(self):
        print('wozuida')
class PaxingAni(Animel):
    def __init__(self):
        print('Paxing Dongwu')
class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('i am init in dog')
# 实例化的时候，自动调用了Dog的构造函数
# 因为找到了构造函数，则不再查找父类的构造函数

kaka = Dog()

print('-' * 70)

# 猫没有构造函数
class Cat(PaxingAni):
    pass
# 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
c = Cat()

print('-' * 70)

# 继承中的构造函数：3

class Animel():
    def __init__(self):
        print('wozuida')
class PaxingAni(Animel):
    def __init__(self,name):
        print('Paxing Dongwu {0}'.format(name))
class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('i am init in dog')
# 实例化Dog时，查找到Dog的构造函数，参数匹配，不报错
d = Dog()

class Cat(PaxingAni):
    pass
# 此时，由于Cat没有构造函数，则向上查找
# 因为PaxingAni的构造函数需要两个参数，实例化的时候给了一个，报错
# 此时需要给name参数赋值，变为实参
c = Cat(name = 'doudou')
