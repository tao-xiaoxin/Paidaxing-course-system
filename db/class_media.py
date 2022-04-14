'''
类管理
'''

from db import db_handle



# 基类
class BaseClass:
    def save(self):
        db_handle.save_date(self)

    @classmethod
    def check(cls,name):
        obj = db_handle.check_obj(cls.__name__,name)
        if obj:
            return obj
        else:
            return False

# 公共类
class Person(BaseClass):
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
        self.course_list = []

# 学生类
class Student(Person):
    def __init__(self,name,passwd):
        super().__init__(name,passwd)
        self.school_campus = ''
        self.course_grade = {}
        self.course_list = []
        self.save()

    # 选课
    def select_course(self,course_obj):
        self.course_list.append(course_obj)
        self.save()

    # 选校区
    def select_campus(self,school_obj):
        self.school_campus = f"{school_obj.name}_{school_obj.campus}"
        self.save()

    # 查看成绩
    def check_grade(self):
        return self.course_grade

    # 查看课程
    def check_course(self):
        return self.course_list

# 老师类
class Teacher(Person):
    def __init__(self,name,passwd):
        super().__init__(name,passwd)
        self.save()

    # 选择教授课程
    def select_course(self,course):
        self.course_list.append(course)
        self.save()

    # 查看教授课程
    def check_course(self):
        return self.course_list

    # 修改学生成绩
    def change_grade(self,stu_obj,course_name,num):
        stu_obj.course_grade[course_name] = num
        stu_obj.save()

# 课程类
class Course(BaseClass):
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period
        self.stu_list = []
        self.save()

    # 添加课程下的学生
    def add_stu(self,stu_obj):
        self.stu_list.append(stu_obj)
        self.save()

    # 查看课程下的学生
    def check_stu_list(self):
        return self.stu_list

# 学校类
class School(BaseClass):
    def __init__(self,name,campus):
        self.name = name
        self.campus = campus
        self.course_list = []
        self.tea_list = []
        self.stu_list = []
        self.save()

    # 添加课程
    def add_course(self,course):
        self.course_list.append(course)
        self.save()

# 管理员类
class Admin(Person):
    def __init__(self,name,passwd):
        super().__init__(name,passwd)
        self.save()

    # 创建老师
    def create_tea(self,name,passwd):
        Teacher(name,passwd)

    # 创建学校
    def create_school(self,name,campus):
        School(name,campus)

    # 创建课程
    def create_course(self,name,price,period):
        Course(name,price,period)




