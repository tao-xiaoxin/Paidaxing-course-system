'''
学生功能接口
'''
import os
from db import class_media
from conf import setting



# 学生选择学校及校区
def selece_school_campus_api(user_name,name,campus):
    school_path = os.path.join(setting.DB_PATH, "School", f"{name}_{campus}.pik")
    if not os.path.isfile(school_path):
        return False, f"{name}学校{campus}校区不存在,请重新选择"
    else:
        user_obj = class_media.Student.check(user_name)
        school_obj = class_media.School.check(f"{name}_{campus}")
        if user_obj.school_campus:
            return False, "你已经选择了学校,无法再进行选择"
        else:
            user_obj.select_campus(school_obj)
            return True, "选择学校成功"

# 学生选择课程
def select_course_api(user_name,name):
    course_path = os.path.join(setting.DB_PATH,"Course",f"{name}.pik")
    if not os.path.isfile(course_path):
        return False, f"{name}课程不存在"
    else:
        user_obj = class_media.Student.check(user_name)
        course_obj = class_media.Course.check(name)
        user_obj.select_course(name)
        course_obj.add_stu(user_name)
        return True, f"{name}课程添加成功"

# 查看成绩接口
def check_grade_api(user_name):
    user_obj = class_media.Student.check(user_name)
    user_grade = user_obj.check_grade()
    if len(user_grade) == 0:
        return False, "该学生成绩还未修改"
    else:
        return True, user_grade