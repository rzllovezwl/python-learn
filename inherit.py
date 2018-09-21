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