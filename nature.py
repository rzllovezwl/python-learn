# coding=utf-8
'''属性案例'''

# 创建Student类，描述学生类
# 学生具有Student.name属性
# 但name格式并不统一
# 可以增加一个函数，然后自动调用的方法，但很蠢

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.setName(name)

    # 介绍下自己
    def intro(self):
        print('he, my name is {0}, my age is{1}'.format(self.name, self.age))
    def setName(self, name):
        self.name = name.upper()
s1 = Student('RENZhenglin', 18)
s2 = Student('zhangwenli', 19)
s1.intro()
s2.intro()

print('-' * 70)

'''property案例'''
# 定义一个Person类，具有name，age属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 年龄，我们希望内部统一使用整数
# x = property（fget，fset，fdel，doc）

class Person():
    # 函数的名称可以任意
    def fget(self):
        return self._name * 2
    def fset(self, name):
        # 所有输入的姓名以大写形式保存
        self._name = name.upper()
    def fdel(self):
        self._name = 'Noname'
    name = property(fget, fset, fdel, 'lulala')
p1 = Person()
p1.name = 'zhangwenli'
print(p1.name)