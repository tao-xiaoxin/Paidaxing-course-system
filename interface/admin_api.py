'''
管理员接口
    注册接口
    登入接口
    查看教授课程接口
    选择教授课程接口
    查看课程下学生接口
    修改学生成绩接口
'''
import os
from db import class_media
from conf import setting


# 创建课程接口
def create_course_api(name,price,period):
    course_path = os.path.join(setting.DB_PATH,"Course",f"{name}.pik")
    if os.path.isfile(course_path):
        return False, f"{name}课程已经存在"
    else:
        class_media.Course(name,price,period)
        return True, f"{name}课程创建成功"


# 创建学校接口
def create_school_api(name,campus):
    school_path = os.path.join(setting.DB_PATH,"School",f"{name}_{campus}.pik")
    if os.path.isfile(school_path):
        return False, f"{name}学校{campus}校区已存在"
    else:
        class_media.School(name,campus)
        return True, f"{name}学校{campus}校区创建成功"