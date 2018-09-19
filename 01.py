'''
定义一个学生类，用啦形容学生
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
print('-' * 60)

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
a.name = 'zhenglin'
a.age = 19

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))