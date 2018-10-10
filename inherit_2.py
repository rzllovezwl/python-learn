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

print('-' * 70)

'''Mixin例子'''
class Person():
    name = 'zhangwenli'
    age = 18

    def eat(self):
        print('EAT......')

    def drink(self):
        print('DRINK......')

    def sleep(self):
        print('SLEEP......')

class Teacher(Person):
    def work(self):
        print('WORK......')

class Student(Person):
    def study(self):
        print('Study')

class Tutor(Teacher, Student):
    pass

t = Tutor()

print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print('*' * 70)

class TeacherMixin():
    def work(self):
        print('Work')

class StudentMixin():
    def study(self):
        print('Study')

class TutorM(Person, TeacherMixin, StudentMixin):
    pass

tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)

print('-' * 70)

'''issubclass'''
class A():
    pass
class B(A):
    pass
class C():
    pass
print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(C, object))

print('-' * 70)

'''isinstance'''
class A():
    pass
a = A()

print(isinstance(a, A))

print('-' * 70)

'''hasattr'''
class A():
    name = 'NoName'
a = A()
print(hasattr(a, 'name'))

print('-' * 70)

'''dir'''
class A():
    pass
print(dir(A))