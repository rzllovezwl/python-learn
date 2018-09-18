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