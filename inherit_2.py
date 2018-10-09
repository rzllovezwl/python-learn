class Fish():
    def __init__(self, name):
        self.name = name
    def swim(self):
        print('i am swimming')
class Bird():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print('i am flying')
class Person():
    def __init__(self, name):
        self.name = name
    def work(self):
        print('working')

'''多继承例子'''
'''子类可以直接拥有父类的属性和方法，私有属性和方法除外'''
class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name
s = SuperMan('yueyue')
s.fly()
s.swim()

print('-' * 70)

'''单继承例子'''
class Student(Person):
    def __init__(self, name):
        self.name = name
stu = Student('weli')
stu.work()

print('-' * 70)

'''菱形继承问题'''
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass