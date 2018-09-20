'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
wenli = Student()

# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1、def的缩紧层级
    # 2、系统默认有一个self参数
    def DoHomework(self):
        print("我在做作业")

        # 推荐在函数末尾使用return语句
        return None
# 实例化一个叫lili的学生，是一个具体的人
lili = PythonStudent()
print(lili.name)
print(lili.age)
# 注意成员函数的调用没有传入参数
lili.DoHomework()
print('-' * 70)

'''
例子：类和对象的成员分析
'''
class A():
    name = 'wenli'
    age = 18

    def say(self):
        self.name = 'aaaa'
        self.age = 200
# 此案例说明：
#   类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，
#   指向同一个变量
# 此时，A称为类实例
print(A.name)
print(A.age)

print('*' * 20)

# id可以鉴别一个变量是否和另一个变量是同一个变量
print(id(A.name))
print(id(A.age))

print('*' * 20)
a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print('-' * 70)
'''
给对象的实例赋值的情况下，属性指向不同变量
'''
# 此时，A称为类实例
print(A.name)
print(A.age)

print('*' * 20)

# id可以鉴别一个变量是否和另一个变量是同一个变量
print(id(A.name))
print(id(A.age))

print('*' * 20)
a = A()
# 查看A内所有的属性
print(A.__dict__)
print(a.__dict__)
a.name = 'zhenglin'
a.age = 19
print(a.__dict__)

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print('-' * 70)

'''
关于self
'''
class Student():
    name = 'wenli'
    age = 18

    def say(self):
        self.name = 'aaaa'
        self.age = 200
        print('my name is {0}'.format(self.name))
        print('my age is {0}'.format(self.age))
renzhenglin = Student()
renzhenglin.say()

print('-' * 70)

class Teacher():
    name = 'wenli'
    age = 19

    def say(self):
        self.name = 'zhenglin'
        self.age = 20
        print('my name is {0}'.format(self.name))
        print('my age is {0}'.format(__class__.age)) #访问类的成员变量用 __class_
    def sayAgain():
        print(__class__.name) #访问类的成员变量用 __class__
        print(__class__.age) #访问类的成员变量用 __class_
        print('hello')
t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()

print('-' * 70)

class A():
    name = 'wenli'
    age = 18

    def __init__(self):
        self.name = 'aaaa'
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = 'zhenglin'
    age = 90

a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()
# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)
# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)
# 以上代码，利用了鸭子模型

print('-' * 70)

# 私有变量案例

class Person():
    # name是公有成员
    name = 'zhenglin'
    # __age就是私有成员
    __age = 18
p = Person
# name是公有变量
print(p.name)
p._Person__age = 19 # 可以更改变量
print(p._Person__age)# name mangling技术可以访问到私有变量
# __age是私有变量
# 注意报错信息
#print(p.__age) 访问不到

# name mangling技术
print(Person.__dict__)